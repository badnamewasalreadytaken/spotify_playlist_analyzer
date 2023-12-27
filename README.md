# **Spotify Playlist Analyzer**

Hello! Welcome to the Spotify Playlist Analyzer with Chart Scraper.

This project was initially conceived as a final project for the Autumn 2023 DATA 6505-02 Data Munging in Python class at Fairfield University. The goal was to develop a means by which one could get a quick statistical summary of a Spotify playlist's songs' audio features, from which analysis on music trends could be conducted over time to determine what constitutes a hit song. This entailed the use of the [Spotipy](https://spotipy.readthedocs.io/) Python package, which integrates the [Spotify Web API](https://developer.spotify.com/documentation/web-api) into Python modules.

The **Playlist Analyzer** notebook retrieves the current tracks of a given Spotify playlist along with their audio features.

The **Chart Scraper** notebook uses a couple of webscrapers to retrieve historical Spotify chart information from charts.spotify.com and metrix.musicstax.com. The audio features of each track are then retrieved, appended to the chart entries and analyzed. The master scraper function is set up for the Daily Top Songs Global chart as of December 2023, but could feasibly be modified for the Weekly Top Songs Chart.

To use the Spotify API through the Spotipy commands in the included notebooks, a [Spotify for Developers](https://developer.spotify.com/) account is required. Further information on the individual functions and variables are included in the notebooks.

**Note:** Per [Section III.14 of the Spotify Developer Policy](https://developer.spotify.com/policy#iii-some-prohibited-applications) and [Section IV.2.a.i. of the Spotify for Developers Terms](https://developer.spotify.com/terms#section-iv-restrictions), any data retrieved using the Spotify API, charts.spotify.com or musicstax.com may not be used to train machine learning models.
