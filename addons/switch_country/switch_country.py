"""
Blue Archive mitmproxy addon for intercepting and analyzing game traffic.

This addon provides basic functionality for:
- Logging Blue Archive API requests and responses
- Pretty-printing JSON data
- Basic traffic analysis

Usage:
    mitmweb -s addons/blue_archive.py
"""

import json
import logging
import base64
import socket
import struct
import random
from urllib.parse import urlparse

from mitmproxy import http
from mitmproxy import ctx
from Crypto.Cipher import AES

DEFAULT_REGION = "ASIA"

def random_ip():
    """Generate a random IP address."""
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

country_region_maps = {
    # nxm-kr-bagl
    "KR": 1,
    # nxm-tw-bagl
    "TW": 4,
    # nxm-th-bagl
    "ASIA": 5,
    # nxm-or-bagl
    "US": 1,
    # nxm-eu-bagl
    "EU": 1,
}

country_code_maps = {
    "KR": "KR",
    "ASIA": "SG",
    "US": "US",
    "TW": "TW",
    "EU": "GB",
}

membership_maps = {
    "KR": [101, 103, 110, 1, 104, 9999],
    "ASIA": [101, 103, 110, 107, 9999],
    "US": [101, 103, 110, 107, 9999],
    "TW": [101, 103, 110, 107, 9999],
    "EU": [101, 103, 110, 107, 9999],
}

class SwitchCountryAddon:
    """Main addon class for Blue Archive traffic analysis."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nexon_m_api_host = "m-api.nexon.com"
        self.nexon_public_host = "public.api.nexon.com"
        self.random_ip = random_ip()
    
    def load(self, loader):
        """Load addon configuration."""
        loader.add_option(
            name="region",
            typespec=str,
            default=DEFAULT_REGION,
            help="Region to switch to"
        )
        loader.add_option(
            name="key",
            typespec=str,
            default="dd4763541be100910b568ca6d48268e3",
            help="Key to encrypt the response"
        )
    
    def response(self, flow: http.HTTPFlow) -> None:
        """Handle HTTP responses."""
        rs = urlparse(flow.request.pretty_url)
        host = rs.hostname
        path = rs.path
        self.logger.info(f"Request Host: {host}, Path: {path}")
        if self._is_nexon_public_country_request(host, path):
            return self._handle_nexon_public_country_request(flow)
        if self._is_nexon_m_api_country_request(host, path):
            return self._handle_nexon_m_api_country_request(flow)
        if self.is_nexon_m_api_enter_toy_request(host, path):
            return self._handle_nexon_m_api_enter_toy_request(flow)
        if self.is_nexon_m_api_ip_request(host, path):
            return self._handle_nexon_m_api_ip_request(flow)
        return
    
    def _handle_nexon_public_country_request(self, flow: http.HTTPFlow) -> None:
        """Handle Nexon public country request."""
        self.logger.info(f"Nexon public country request received: {flow.request.pretty_url}")
        # Make it singleton for all requests
        response_json = {"ip": self.random_ip, "country-code": self.country_code(ctx.options.region)}
        response_json = json.dumps(response_json, ensure_ascii=False, separators=(',', ':'))
        self.logger.info(f"Response: {response_json}")
        flow.response.content = response_json.encode()
        return
    
    def country_code(self, region: str) -> str:
        """Get the country code for the region."""
        return country_code_maps[region.upper()]
    
    def country_region(self, region: str) -> int:
        """Get the country region for the region."""
        return country_region_maps[region.upper()]
    
    def membership(self, region: str) -> list:
        """Get the membership for the region."""
        return membership_maps[region.upper()]
    
    def _handle_nexon_m_api_country_request(self, flow: http.HTTPFlow) -> None:
        """Handle Nexon m-api country request."""
        self.logger.info(f"Nexon getCountry Response received: {flow.response.status_code} {flow.response.reason}")
        response = {"errorCode":0,"result":{"country":self.country_code(ctx.options.region)},"errorText":"成功","errorDetail":""}
        # Encrypt the response
        response_json = json.dumps(response, ensure_ascii=False, separators=(',', ':'))
        # From hex to bytes
        encrypted_response = self.encrypt(response_json, bytes.fromhex(ctx.options.key))
        self.logger.info(f"Encrypted response: {base64.b64encode(encrypted_response).decode()}")
        # Set the response content as bytes
        flow.response.content = encrypted_response

    def _is_nexon_public_country_request(self, host: str, route: str) -> bool:
        """Check if request is related to get country."""
        return host == self.nexon_public_host and route == "/toy/v2/country"

    def _is_nexon_m_api_country_request(self, host: str, route: str) -> bool:
        """Check if request is related to get country."""
        return host == self.nexon_m_api_host and route == "/sdk/getCountry.nx"
    
    def is_nexon_m_api_enter_toy_request(self, host: str, route: str) -> bool:
        """Check if request is related to enter toy."""
        return host == self.nexon_m_api_host and route == "/sdk/enterToy.nx"

    def is_nexon_m_api_ip_request(self, host: str, route: str) -> bool:
        """Check if request is related to get ip."""
        return host == self.nexon_m_api_host and route == "/sdk/getIp.nx"

    def _handle_nexon_m_api_ip_request(self, flow: http.HTTPFlow) -> None:
        """Handle Nexon m-api ip request."""
        self.logger.info(f"Nexon getIp Response received: {flow.response.status_code} {flow.response.reason}")
        response = {"errorCode":0,"result":{"ip":self.random_ip},"errorText":"成功","errorDetail":""}
        response_json = json.dumps(response, ensure_ascii=False, separators=(',', ':'))
        flow.response.content = response_json.encode()
        return

    def _handle_nexon_m_api_enter_toy_request(self, flow: http.HTTPFlow) -> None:
        """Handle Nexon m-api enter toy request."""
        self.logger.info(f"Nexon enter toy request received: {flow.request.pretty_url}")
        # Get the request body
        response_json = flow.response.json()
        self.logger.info(f"Response body: {response_json}")
        updated_result = self._update_toy_response(response_json)
        self.logger.info(f"Updated result: {updated_result}")
        flow.response.content = json.dumps(updated_result, ensure_ascii=False, separators=(',', ':')).encode()
        return

    def _update_toy_response(self, response_json: dict) -> dict:
        """Update the toy response."""
        # 1. Update result.country: KR, HK
        # 2. Update result.userArenaRegion: 1 (KR), 4 (HMT)
        # 3. Update result.service.nxkATL: 1 (KR only)
        # 4. Update result.service.useMemberships: [101, 103, 110, 1, 104, 9999] (KR Only), [101, 103, 110, 107, 9999] (Others)
        result = response_json.get("result")
        result["country"] = self.country_code(ctx.options.region)
        result["userArenaRegion"] = self.country_region(ctx.options.region)
        if ctx.options.region == "KR":
            result["service"]["nxkATL"] = 1
        elif "nxkATL" in result["service"]:
            del result["service"]["nxkATL"]
        result["service"]["useMemberships"] = self.membership(ctx.options.region)
        return response_json

    def encrypt(self, data: str, key: bytes) -> bytes:
        """Encrypt the data using the key with PKCS7 padding."""
        # Convert string to bytes
        data_bytes = data.encode('utf-8')
        
        # Add PKCS7 padding to align to 16-byte blocks
        block_size = AES.block_size  # 16 bytes for AES
        padding_length = block_size - (len(data_bytes) % block_size)
        padding = bytes([padding_length] * padding_length)
        padded_data = data_bytes + padding
        
        # Use AES-128-ECB to encrypt the data
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(padded_data)
    
# Required for mitmproxy to load the addon
addons = [SwitchCountryAddon()] 