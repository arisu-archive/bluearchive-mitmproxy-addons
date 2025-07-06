# Arisu Archive Mitmproxy Addons

<p align="center">
  <h3 align="center">Arisu Archive Mitmproxy Addons</h3>
  <p align="center">
    A collection of mitmproxy addons for debugging and developing Arisu Archive related projects.
    <br />
    <a href="https://github.com/arisu-archive/bluearchive-mitmproxy-addons/issues">Report Bug</a>
    ·
    <a href="https://github.com/arisu-archive/bluearchive-mitmproxy-addons/issues">Request Feature</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/github/issues/arisu-archive/bluearchive-mitmproxy-addons" alt="GitHub Issues">
  <img src="https://img.shields.io/github/forks/arisu-archive/bluearchive-mitmproxy-addons" alt="GitHub Forks">
  <img src="https://img.shields.io/github/stars/arisu-archive/bluearchive-mitmproxy-addons" alt="GitHub Stars">
  <img src="https://img.shields.io/github/last-commit/arisu-archive/bluearchive-mitmproxy-addons" alt="Last Commit">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#notice">Notice</a></li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#addons">Available Addons</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Notice

This project is for educational and development purposes only. Please respect the game's Terms of Service and use these tools responsibly.

## About The Project

This repository hosts a collection of **mitmproxy** addons specifically designed for debugging and development of [Arisu Archive](https://github.com/arisu-archive) related projects, with a primary focus on the mobile game **Blue Archive**.

These addons provide powerful tools to:
- **Intercept and analyze** Blue Archive network traffic
- **Inspect API requests and responses** in real-time
- **Debug client-server communication** issues
- **Develop and test** new features for Blue Archive tools
- **Extract game data** for research and archival purposes

> **⚠️ Important Notice**: This project is for educational and development purposes only. Please respect the game's Terms of Service and use these tools responsibly.

### Features

- 🔍 **Traffic Analysis**: Real-time inspection of Blue Archive API calls
- 📊 **Data Extraction**: Automatic parsing and export of game data
- 🛠️ **Development Tools**: Utilities for Blue Archive mod development
- 📱 **Mobile Support**: Works with both Android and iOS devices
- 🌐 **Web Interface**: Beautiful web UI via mitmweb
- 📝 **Logging**: Comprehensive logging of all intercepted traffic
- 🔄 **Request Modification**: Ability to modify requests on-the-fly
- 💾 **Data Export**: Multiple export formats (JSON, CSV, XML)

### Built With

- [Python 3.9+](https://www.python.org/)
- [mitmproxy](https://mitmproxy.org/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [aiohttp](https://docs.aiohttp.org/)

## Getting Started

### Prerequisites

Ensure you have the following software installed:

- **Python 3.9 or higher**
- **mitmproxy 8.0+**: Install via pip:
  ```sh
  pip install mitmproxy
  ```

### System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 1GB free space for logs and data
- **Network**: Ability to configure proxy settings on target device

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/arisu-archive/mitmproxy-addon.git
   ```

2. **Navigate to the project directory**:
   ```sh
   cd mitmproxy-addon
   ```

3. **Install Python dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Verify installation**:
   ```sh
   mitmdump --version
   ```

## Usage

### Quick Start

1. **Start mitmproxy with the Blue Archive addon**:
   ```sh
   mitmweb -s addons/blue_archive.py -p 8080
   ```

2. **Configure your device**:
   - Set proxy to your computer's IP address on port 8080
   - Install the mitmproxy certificate
   - Access the web interface at `http://127.0.0.1:8081`

3. **Start Blue Archive** on your device and watch the traffic flow!

### Device Configuration

#### Android
1. Go to **Settings** > **Wi-Fi**
2. Long press your network and select **Modify Network**
3. Set proxy to **Manual** and enter your computer's IP and port 8080
4. Install the certificate from `mitm.it` in your browser

#### iOS
1. Go to **Settings** > **Wi-Fi**
2. Tap the (i) icon next to your network
3. Scroll down and configure **HTTP Proxy** to **Manual**
4. Enter your computer's IP and port 8080
5. Install the certificate from `mitm.it` in Safari

### Command Line Options

```sh
# Start with specific addon
mitmweb -s addons/blue_archive.py

# Start with multiple addons
mitmweb -s addons/blue_archive.py -s addons/data_extractor.py

# Start with custom port
mitmweb -s addons/blue_archive.py -p 8080

# Start with logging
mitmweb -s addons/blue_archive.py --set confdir=~/.mitmproxy
```

## Available Addons

### 🎮 Blue Archive Core (`blue_archive.py`)
- **Purpose**: Main addon for Blue Archive traffic analysis
- **Features**: 
  - Request/response logging
  - JSON pretty-printing
  - Basic data extraction
- **Status**: ✅ Implemented

### 📊 Data Extractor (`data_extractor.py`)
- **Purpose**: Extract and organize game data
- **Features**:
  - Character data extraction
  - Equipment information
  - Event data parsing
- **Status**: 🚧 In Development

### 🔧 Developer Tools (`dev_tools.py`)
- **Purpose**: Development utilities for modders
- **Features**:
  - Request modification
  - Response simulation
  - Debug logging
- **Status**: 📋 Planned

### 🌐 Web Dashboard (`dashboard.py`)
- **Purpose**: Enhanced web interface for data visualization
- **Features**:
  - Real-time charts
  - Data export tools
  - Custom filtering
- **Status**: 📋 Planned

## Troubleshooting

### Common Issues

#### Certificate Installation Problems
**Issue**: Browser shows "Your connection is not private"
**Solution**: 
1. Visit `mitm.it` in your browser
2. Download and install the certificate for your platform
3. On iOS, go to Settings > General > About > Certificate Trust Settings
4. Enable full trust for the mitmproxy certificate

#### No Traffic Captured
**Issue**: mitmproxy shows no requests from Blue Archive
**Solution**:
1. Verify proxy settings are correct
2. Check if certificate is properly installed
3. Ensure Blue Archive is not using certificate pinning bypass
4. Try restarting the game after proxy configuration

#### Performance Issues
**Issue**: Game runs slowly or times out
**Solution**:
1. Reduce logging verbosity
2. Use `mitmdump` instead of `mitmweb` for better performance
3. Increase system resources
4. Filter specific endpoints only

### Getting Help

If you encounter issues:
1. Check the [FAQ](#faq) section below
2. Search existing [GitHub Issues](https://github.com/arisu-archive/mitmproxy-addon/issues)
3. Create a new issue with detailed information

## FAQ

### General Questions

**Q: Is this legal to use?**
A: These tools are for educational and development purposes. Always respect the game's Terms of Service and applicable laws.

**Q: Will this get my account banned?**
A: While the tools only passively monitor traffic, use at your own risk. We recommend using test accounts.

**Q: Does this work with other games?**
A: The addons are specifically designed for Blue Archive, but the techniques can be adapted for other games.

### Technical Questions

**Q: What data can I extract?**
A: You can extract any data transmitted between the game client and server, including character stats, equipment, and event information.

**Q: Can I modify game requests?**
A: Yes, advanced addons can modify requests, but this requires careful implementation to avoid breaking the game.

**Q: How do I contribute new addons?**
A: See our [Contributing Guide](CONTRIBUTING.md) for detailed instructions on addon development.

## Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** and suggest improvements
- 📝 **Improve documentation** and add examples
- 🔧 **Develop new addons** for different use cases
- 🌍 **Translate** documentation to other languages
- 🎨 **Design** better UI/UX for web interface
- 📊 **Share datasets** (with proper anonymization)

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies (`pip install -r requirements-dev.txt`)
4. Make your changes and add tests
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

- **mitmproxy**: MIT License
- **aiohttp**: Apache License 2.0
- **Python**: Python Software Foundation License

---

<p align="center">
  <i>Made with ❤️ by the Arisu Archive Team</i>
</p>
