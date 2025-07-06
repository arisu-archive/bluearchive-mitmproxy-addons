# Blue Archive Country Switch Addon

A mitmproxy addon that uses **WireGuard VPN mode** to intercept and modify Blue Archive country detection responses, allowing you to switch your apparent country/region for the game.

## 🎯 Purpose

This addon intercepts Blue Archive's country detection API calls and returns a modified response with your desired country code. This can be useful for:

- **Region Testing**: Test how the game behaves in different regions
- **Development**: Develop region-specific features
- **Research**: Analyze regional differences in game content
- **Troubleshooting**: Debug region-related issues

## ⚠️ Important Notice

**This addon is for educational and development purposes only.** Please respect Blue Archive's Terms of Service and use this tool responsibly. Use of this addon may violate the game's terms of service and could result in account suspension.

## 🚀 Features

- 🌍 **Region Switching**: Change your apparent country/region
- 🔐 **Response Encryption**: Properly encrypts responses using AES-128-ECB
- 🛡️ **WireGuard VPN**: Uses WireGuard protocol for secure traffic interception
- 🎛️ **Configurable**: Easy configuration via command line options
- 📝 **Logging**: Detailed logging for debugging
- 🔒 **Secure**: Uses proper PKCS7 padding for encryption

## 📋 Prerequisites

- **Python 3.9+**
- **mitmproxy 8.0+**
- **pycryptodome** (for AES encryption)

## 🛠️ Installation

1. **Navigate to the addon directory**:
   ```bash
   cd addons/switch_country
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python -c "from Crypto.Cipher import AES; print('Dependencies OK')"
   ```

## 🎮 Usage

### Basic Usage

Start mitmproxy with the switch_country addon:

```bash
# Using the provided start script (recommended)
./start.sh

# Or manually with mitmweb
mitmweb -s switch_country.py -m wireguard --listen-host 0.0.0.0 --listen-port 51820 --ignore-hosts "^ba.dn.nexoncdn.co.kr|^toy.log.nexon.io"

# Using mitmdump (command line)
mitmdump -s switch_country.py -m wireguard --listen-host 0.0.0.0 --listen-port 51820 --ignore-hosts "^ba.dn.nexoncdn.co.kr|^toy.log.nexon.io"

# Using mitmproxy (interactive)
mitmproxy -s switch_country.py -m wireguard --listen-host 0.0.0.0 --listen-port 51820 --ignore-hosts "^ba.dn.nexoncdn.co.kr|^toy.log.nexon.io"
```

### Configuration Options

The addon supports several configuration options:

```bash
# Set country code (default: HK)
mitmweb -s switch_country.py --set region=JP

# Set custom encryption key (default: dd4763541be100910b568ca6d48268e3)
mitmweb -s switch_country.py --set key=your_custom_key_here --set region=JP

# Multiple options
mitmweb -s switch_country.py --set region=US --set key=dd4763541be100910b568ca6d48268e3
```

### Supported Regions

Common regions you can use:
- `ASIA` - Asia
- `US` - United States
- `EU` - Europe
- `KR` - South Korea
- `TW` - Taiwan

## 🔧 Configuration

### Command Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `region` | string | `ASIA` | Region to switch to |
| `key` | string | `dd4763541be100910b568ca6d48268e3` | Hex-encoded encryption key |

### Examples

```bash
# Switch to Japan region
mitmweb -s switch_country.py --set region=JP

# Switch to US region with custom key
mitmweb -s switch_country.py --set region=US --set key=your_key_here

# Enable debug logging
mitmweb -s switch_country.py --set region=HK -v
```

## 📱 Device Setup

### WireGuard Configuration

This addon uses **WireGuard mode** listening on port **51820**. You need to configure your device to use WireGuard VPN.

### Android

1. **Install WireGuard**:
   - Install WireGuard app from Google Play Store

2. **Configure VPN**:
   - Open WireGuard app
   - Add a new tunnel configuration
   - Set server endpoint to your computer's IP and port `51820`
   - Configure the tunnel according to your network setup

3. **Install Certificate**:
   - Open browser and go to `mitm.it`
   - Download and install the Android certificate
   - Go to **Settings** > **Security** > **Trusted Credentials**
   - Verify the certificate is installed

### iOS

1. **Install WireGuard**:
   - Install WireGuard app from App Store

2. **Configure VPN**:
   - Open WireGuard app
   - Add a new tunnel configuration
   - Set server endpoint to your computer's IP and port `51820`
   - Configure the tunnel according to your network setup

3. **Install Certificate**:
   - Open Safari and go to `mitm.it`
   - Download and install the iOS certificate
   - Go to **Settings** > **General** > **About** > **Certificate Trust Settings**
   - Enable full trust for the mitmproxy certificate

## 🔍 How It Works

### Technical Details

1. **Intercepts Requests**: The addon monitors all HTTP traffic for requests to `m-api.nexon.com` endpoints ending with `/sdk/getCountry.nx`

2. **Modifies Response**: When a matching request is found, it:
   - Creates a new response with the desired country code
   - Encrypts the response using AES-128-ECB with PKCS7 padding
   - Replaces the original response

3. **Encryption Process**:
   ```python
   response = {"errorCode": 0, "result": {"country": "SG"}, "errorText": "成功", "errorDetail": ""}
   json_response = json.dumps(response)
   encrypted_response = aes_encrypt(json_response, key)
   ```

### Response Format

The addon returns a JSON response in this format:
```json
{
  "errorCode": 0,
  "result": {
    "country": "SG"
  },
  "errorText": "成功",
  "errorDetail": ""
}
```

## 🐛 Troubleshooting

### Common Issues

#### No Traffic Intercepted
**Problem**: The addon doesn't seem to be working
**Solution**:
1. Verify WireGuard VPN configuration on your device
2. Check certificate installation
3. Ensure Blue Archive is making country detection requests
4. Check mitmproxy logs for errors
5. Verify WireGuard connection is active

#### Encryption Errors
**Problem**: "Data must be aligned to block boundary" error
**Solution**: 
- This is fixed in the latest version with proper PKCS7 padding
- Ensure you're using the latest version of the addon

#### Game Connection Issues
**Problem**: Blue Archive won't connect or shows network errors
**Solution**:
1. Verify the encryption key is correct
2. Check that the response format matches what the game expects
3. Try restarting the game after WireGuard VPN configuration
4. Ensure WireGuard tunnel is properly configured and connected

### Debug Mode

Enable verbose logging to see what's happening:

```bash
mitmweb -s switch_country.py -m wireguard --listen-host 0.0.0.0 --listen-port 51820 --ignore-hosts "^ba.dn.nexoncdn.co.kr|^toy.log.nexon.io" -v
```

Check the logs for messages like:
- `Nexon getCountry Response received`
- `Encrypted response: [base64 data]`

## 📊 Example Session

Here's what a typical session looks like:

```bash
$ ./start.sh
Loading script switch_country.py
WireGuard server listening at 0.0.0.0:51820
Web server listening at http://127.0.0.1:8081/

# Configure WireGuard VPN on your device to connect to your server
# Start Blue Archive on your device
# The addon will intercept country detection requests and return your configured region
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Issues**: Found a bug? Create an issue
2. **Improve Code**: Submit pull requests with improvements
3. **Add Features**: Enhance the addon with new functionality
4. **Documentation**: Help improve this README

### Development Setup

```bash
# Clone the repository
git clone https://github.com/arisu-archive/bluearchive-mitmproxy-addons.git
cd bluearchive-mitmproxy-addons/addons/switch_country

# Install development dependencies
pip install mitmproxy pycryptodome pytest

# Run tests (if available)
pytest
```

## ⚖️ Legal Disclaimer

This addon is provided for educational and development purposes only. The developers are not responsible for any consequences resulting from the use of this tool. Users are responsible for ensuring their use complies with all applicable terms of service and laws.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## 🙏 Acknowledgments

- **mitmproxy team** for the excellent proxy framework
- **Blue Archive developers** for creating the game
- **pycryptodome** for providing robust encryption tools
- **Community contributors** for testing and feedback

---

<p align="center">
  <i>Made with ❤️ for the Blue Archive community</i>
</p>
