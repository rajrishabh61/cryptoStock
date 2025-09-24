<h1 align="center">🚀 CryptoStock Tracker</h1>

<p align="center">
  A Python web scraper to track cryptocurrency prices, 24h changes, and market caps from <a href="https://www.coingecko.com/" target="_blank">CoinGecko</a>. Stay updated with the latest crypto market trends in a structured CSV format! 📈
</p>

<h2>✨ Features</h2>
<ul>
  <li>Scrapes live crypto data from CoinGecko</li>
  <li>Captures <strong>Coin Name</strong>, <strong>Price</strong>, <strong>24h Change</strong>, and <strong>Market Cap</strong></li>
  <li>Prevents duplicate entries for clean data</li>
  <li>Outputs results to a CSV file for easy analysis</li>
  <li>Simple and lightweight Python implementation using <code>BeautifulSoup</code> and <code>requests</code></li>
</ul>

<h2>⚡ Usage</h2>
<pre>
from cryptoStock import cryptoStock

crypto = cryptoStock()
crypto.crypsto()
</pre>

<h2>💡 Installation</h2>
<pre>
pip install beautifulsoup4 requests
</pre>

<h2>🔗 Link</h2>
<p>
Check the live repo: <a href="https://github.com/rajrishabh61/cryptoStock" target="_blank">cryptoStock on GitHub</a>
</p>

<h2>📊 Output Example</h2>
<pre>
Coin || Price || 24h Change || Market Cap
Bitcoin || 29400 || +2.5% || $565B
Ethereum || 1850 || -1.2% || $223B
...
</pre>

<p align="center">
  Made with ❤️ by <strong>Rishabh Bajaj</strong>
</p>
