<a name="readme-top"></a>

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/PMJeffery/street-address-to-lat-long">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

<p align="center">
    project_description
    <br />
    <a href="https://github.com/PMJeffery/street-address-to-lat-long"><strong>Explore the docs »</strong></a>
    <br />
    <br />
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Ever need to convert a list of Street Addresses to Latitude and Longitude coordinates?  

Run this simple Python 3 script to import a list of your addresses and output the addresses with their respective latitude and longitude coordinates in a CSV file format.

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python Versions][pyversion-button]][md-pypi]
* [![BSD License][bsdlicense-button]][bsdlicense]
* [pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
* [bsdlicense-button]: https://img.shields.io/badge/license-BSD-yellow.svg

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

Open "addresses.txt" and paste your address.  One address per line.

The format must be <street address>,<city>,<state/territory/provence>,<country>

Example: *1600 Pennsylvania Avenue NW, Washington, DC 20500, United States*

```sh
python3 address2latlong.py
```

Depending upon how many addresses you have entered, it may take more than several seconds to return the results.  If you have a large data set or you rapidly run the script many times, you may get an error regarding excessive API usage.

If you are getting excessive API usage errors, either slice your input file into multiple files or switch to another [geocoder](https://github.com/DenisCarriere/geocoder/tree/master/geocoder) - be sure to read the python code for how to access the geocoder API and adjust the python code accordingly. 

Note that some geocoders may require a login or paid-subscription for higher or unlimited API calls. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
