# CitiBikeNYC
## A deep analysis of the bike sharing network of New York City
The data can be downloaded from the <a href="https://ride.citibikenyc.com/system-data">official CitiBike webiste</a>. There’s a file for each month, a zip file containing a single csv file. The files are in chronological order starting in 2013, so to find the recent ones you have to scroll down. Don’t scroll down all the way to the bottom though; the files with JC in the name are for Jersey City, not New York.

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

## Short links to contents
* [Project proposal](url)
* [Slides](url)
* [Codes](url)
* [Final report](url)

## Additional resources
* Citi Bike publishes real-time system data in <a href="https://github.com/NABSA/gbfs/blob/master/gbfs.md">General Bikeshare Feed Specification format</a>. Get the GBFS feed <a href="http://gbfs.citibikenyc.com/gbfs/gbfs.json">here</a>.
* A group of peaople working with data feeds from NYC's Bike Share system and other bike data maintain <a href="https://groups.google.com/forum/#!aboutgroup/citibike-hackers">this Google Group</a>.
* [Exploring NYC Bike Share Data](https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c) by Clif Kranish(Jan 25, 2021)
* [A Tale of Twenty-Two Million Citi Bike Rides](https://toddwschneider.com/posts/a-tale-of-twenty-two-million-citi-bikes-analyzing-the-nyc-bike-share-system/) by Todd W. Schneider(Jan 13, 2016)
