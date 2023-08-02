<a name="readme-top"></a>
<!-- PROJECT LOGO -->

<br />
<div align="left">

<h3 align="center">Street Address to Latitude Longitude</h3>

<p align="center">
      ·
    <a href="https://github.com/PMJeffery/street-address-to-lat-long/issues">Report Bug</a>
    ·
    <a href="https://github.com/PMJeffery/street-address-to-lat-long/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
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
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project


Ever need to convert a list of Street Addresses to Latitude and Longitude coordinates?  

Run this simple Python 3 script to import a list of your addresses, 'addresses.txt' and output will include a header, addresses with their respective latitude and longitude coordinates in a CSV file format, 'output.csv'

The output file can then be renamed and uploaded to Splunk as a lookup table in a search.

Key Apps to help with managing Lookup Tables and Splunk Configurations, respectively:

[Splunk App for Lookup File Editing](https://splunkbase.splunk.com/app/1724) | [Config Explorer (not compatible with Splunk Cloud)](https://splunkbase.splunk.com/app/4353)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Python 3

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This script is designed to work in Linux, MacOS and Windows with Python3 installed.

Assumption: Python and Git are installed on your system.

### Prerequisites

Install the latest version of [geopy](https://github.com/geopy/geopy)

* pip
  
  ```sh
  pip install geopy
  ```

### Installation

1. Simple: Copy/Paste the [python code](https://raw.githubusercontent.com/PMJeffery/street-address-to-lat-long/main/address2latlong.py)

2. Via 'git' command clone the repo
   
   ```sh
   git clone https://github.com/PMJeffery/street-address-to-lat-long.git
   ```

<!-- USAGE EXAMPLES -->

## Usage


'addresses.txt' provides a sample of publicly available street addresses of Splunk offices around the world.  To test the output, you can run the command as is - shown below and verfiy 'output.csv'

Open 'addresses.txt' and paste your address.  One address per line.

The format must be <street address>,<city>,<state/territory/provence>,<country>

Example: *1600 Pennsylvania Avenue NW, Washington, DC 20500, United States*

```sh
python3 address2latlong.py
```
Results will generate a CSV file, 'output.csv'

Depending upon how many addresses you have entered, it may take more than several seconds to return the results.  If you have a large data set or you rapidly run the script many times, you may get an error regarding excessive API usage.

If you are getting excessive API usage errors, either slice your input file into multiple files or switch to another [geocoder](https://github.com/DenisCarriere/geocoder/tree/master/geocoder) - be sure to read the python code for how to access the geocoder API and adjust the python code accordingly. 

Note that some geocoders may require a login or paid-subscription for higher or unlimited API calls. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
