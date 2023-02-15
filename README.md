# COMP0034 Coursework 1

This repository is created for COMP0034 Coursework 1 done by Team 18. This README.md will provide a guidance for readers
 / markers to facilitate understanding the contents.

# Set-up instructions

1. URL to your GitHub repo: https://github.com/ucl-comp0035/comp0034-cw1-g-team18.git;
2. Please install all necessary Python packages listed in [requirements.txt](requirements.txt);
3. The [business-need.pdf](business-need.pdf), [requirements.pdf](requirements.pdf) and [design.pdf](design.pdf) documents 
are collected from previous work of the team in COMP0035 last term. These files are used to help understand the context 
and initial design of the Web APP;
4. Browser used to test the Dash created in this coursework is Chrome 109 version and our group members use Mac OS, 
the chromedriver is downloaded to [chromedriver_mac_arm64](test/chromedriver_mac_arm64) directory under [test](test) 
folder. You may need to execute it first before going to testing;
5. The CI workflow was implemented during a early stage of the project but failed attempts were deleted, you may find 
evidences through commit history to show we have regularly used CI approaches.

# 1. Visualisation design

See [VisualizationDesign.pdf](VisualizationDesign.pdf)

# 2. Dash app

The code for the Dash app can be found at [gender_pay_gap_dash_app.py](src/gender_pay_gap_dash_app/gender_pay_gap_dash_app.py).

In order to make the app look more aesthetically pleasing, a CSS [stylesheet](src/gender_pay_gap_dash_app/assets/style.css) 
can be found under [assets](src/gender_pay_gap_dash_app/assets) directory in [src](src). It has managed to change the theme 
color and make visualizations in a card style.

Since visualizations require more complex data structure than we thought before during data processing stage at COMP0035
, further data processing was implemented for this coursework. Code for data processing can be looked at [data_prep.py](data_prep.py)
. Meanwhile, we found it easier to split dataframes that we need when generating visualizations, therefore, we have used 
multiple datasets which can be found in [data](src/gender_pay_gap_dash_app/data) directory under src/gender_pay_gap_dash_app 
directory. The dataset we prepared in COMP0035 is [gender_pay_gap_prepared.csv](src/gender_pay_gap_dash_app/data/gender_pay_gap_prepared.csv) 
while all the remaining spreadsheets are created at this time.

Generally, the APP has met requirements that we intended to achieve as a dashboard showing general information of UK 
gender pay gap situations and target users can obtain information to answers their problems. While the map graphs would 
be better with a Choropleth map, we failed to find a proper geojson of UK, thus were unable to create one. Therefore, we 
have used a scatter_mapbox as a substitute by manually inputting the geographical coordinates (longitude and latitude) of 
each region (shown in [data_prep.py](data_prep.py).

# 3. Testing


