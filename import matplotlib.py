
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_column',100)
pd.set_option('display.max_row',20)
df = pd.read_csv('netflix_titles.csv')
df.head()
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	description
0	s1	Movie	Dick Johnson Is Dead	Kirsten Johnson	NaN	United States	September 25, 2021	2020	PG-13	90 min	Documentaries	As her father nears the end of his life, filmm...
1	s2	TV Show	Blood & Water	NaN	Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...	South Africa	September 24, 2021	2021	TV-MA	2 Seasons	International TV Shows, TV Dramas, TV Mysteries	After crossing paths at a party, a Cape Town t...
2	s3	TV Show	Ganglands	Julien Leclercq	Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...	NaN	September 24, 2021	2021	TV-MA	1 Season	Crime TV Shows, International TV Shows, TV Act...	To protect his family from a powerful drug lor...
3	s4	TV Show	Jailbirds New Orleans	NaN	NaN	NaN	September 24, 2021	2021	TV-MA	1 Season	Docuseries, Reality TV	Feuds, flirtations and toilet talk go down amo...
4	s5	TV Show	Kota Factory	NaN	Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...	India	September 24, 2021	2021	TV-MA	2 Seasons	International TV Shows, Romantic TV Shows, TV ...	In a city of coaching centers known to train I...
df.columns
Index(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description'],
      dtype='object')
df.dtypes
show_id         object
type            object
title           object
director        object
cast            object
country         object
date_added      object
release_year     int64
rating          object
duration        object
listed_in       object
description     object
dtype: object
df.shape
(8807, 12)
df.isna().sum()
show_id            0
type               0
title              0
director        2634
cast             825
country          831
date_added        10
release_year       0
rating             4
duration           3
listed_in          0
description        0
dtype: int64
df.loc[df.duplicated()]
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	description
df.loc[df.duplicated(subset=['director'])].dropna()
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	description
52	s53	Movie	InuYasha the Movie 3: Swords of an Honorable R...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2003	TV-14	99 min	Action & Adventure, Anime Features, Internatio...	The Great Dog Demon beaqueathed one of the Thr...
53	s54	Movie	InuYasha the Movie 4: Fire on the Mystic Island	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2004	TV-PG	88 min	Action & Adventure, Anime Features, Internatio...	Ai, a young half-demon who has escaped from Ho...
54	s55	Movie	InuYasha the Movie: Affections Touching Across...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2001	TV-PG	100 min	Action & Adventure, Anime Features, Internatio...	A powerful demon has been sealed away for 200 ...
58	s59	Movie	Naruto Shippûden the Movie: The Will of Fire	Masahiko Murata	Junko Takeuchi, Chie Nakamura, Kazuhiko Inoue,...	Japan	September 15, 2021	2009	TV-PG	96 min	Action & Adventure, Anime Features, Internatio...	When four out of five ninja villages are destr...
59	s60	Movie	Naruto Shippuden: The Movie	Hajime Kamegaki	Junko Takeuchi, Chie Nakamura, Yoichi Masukawa...	Japan	September 15, 2021	2007	TV-PG	95 min	Action & Adventure, Anime Features, Internatio...	The adventures of adolescent ninja Naruto Uzum...
...	...	...	...	...	...	...	...	...	...	...	...	...
8793	s8794	Movie	Yours, Mine and Ours	Raja Gosnell	Dennis Quaid, Rene Russo, Sean Faris, Katija P...	United States	November 20, 2019	2005	PG	88 min	Children & Family Movies, Comedies	When a father of eight and a mother of 10 prep...
8794	s8795	Movie	اشتباك	Mohamed Diab	Nelly Karim, Hany Adel, Tarek Abdel Aziz, Ahme...	Egypt, France	October 11, 2018	2016	TV-14	98 min	Dramas, Independent Movies, International Movies	Amid the tumult following Egyptian President M...
8799	s8800	Movie	Zenda	Avadhoot Gupte	Santosh Juvekar, Siddharth Chandekar, Sachit P...	India	February 15, 2018	2009	TV-14	120 min	Dramas, International Movies	A change in the leadership of a political part...
8802	s8803	Movie	Zodiac	David Fincher	Mark Ruffalo, Jake Gyllenhaal, Robert Downey J...	United States	November 20, 2019	2007	R	158 min	Cult Movies, Dramas, Thrillers	A political cartoonist, a crime reporter and a...
8804	s8805	Movie	Zombieland	Ruben Fleischer	Jesse Eisenberg, Woody Harrelson, Emma Stone, ...	United States	November 1, 2019	2009	R	88 min	Comedies, Horror Movies	Looking to survive in a world taken over by zo...
1465 rows × 12 columns

df.query('director=="Toshiya Shinohara"')
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	description
51	s52	Movie	InuYasha the Movie 2: The Castle Beyond the Lo...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Mieko Harada...	Japan	September 15, 2021	2002	TV-14	99 min	Action & Adventure, Anime Features, Internatio...	With their biggest foe seemingly defeated, Inu...
52	s53	Movie	InuYasha the Movie 3: Swords of an Honorable R...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2003	TV-14	99 min	Action & Adventure, Anime Features, Internatio...	The Great Dog Demon beaqueathed one of the Thr...
53	s54	Movie	InuYasha the Movie 4: Fire on the Mystic Island	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2004	TV-PG	88 min	Action & Adventure, Anime Features, Internatio...	Ai, a young half-demon who has escaped from Ho...
54	s55	Movie	InuYasha the Movie: Affections Touching Across...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 15, 2021	2001	TV-PG	100 min	Action & Adventure, Anime Features, Internatio...	A powerful demon has been sealed away for 200 ...
7088	s7089	Movie	Inuyasha the Movie - L'isola del fuoco scarlatto	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 1, 2017	2004	TV-PG	88 min	Action & Adventure, Anime Features, Internatio...	Ai, a young half-demon who has escaped from Ho...
7089	s7090	Movie	Inuyasha the Movie - La spada del dominatore d...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 1, 2017	2003	TV-14	99 min	Action & Adventure, Anime Features, Internatio...	The Great Dog Demon beaqueathed one of the Thr...
7090	s7091	Movie	InuYasha: The Movie 2: The Castle Beyond the L...	Toshiya Shinohara	Kappei Yamaguchi, Satsuki Yukino, Koji Tsujita...	Japan	September 1, 2017	2002	TV-14	99 min	Action & Adventure, Anime Features, Internatio...	With their biggest foe seemingly defeated, Inu...
df.type.value_counts()
type
Movie      6131
TV Show    2676
Name: count, dtype: int64
df.rating.value_counts()
rating
TV-MA       3207
TV-14       2160
TV-PG        863
R            799
PG-13        490
TV-Y7        334
TV-Y         307
PG           287
TV-G         220
NR            80
G             41
TV-Y7-FV       6
NC-17          3
UR             3
74 min         1
84 min         1
66 min         1
Name: count, dtype: int64
#director with most title
df.director.value_counts()
director
Rajiv Chilaka                     19
Raúl Campos, Jan Suter            18
Marcus Raboy                      16
Suhas Kadav                       16
Jay Karas                         14
                                  ..
Raymie Muzquiz, Stu Livingston     1
Joe Menendez                       1
Eric Bross                         1
Will Eisenberg                     1
Mozez Singh                        1
Name: count, Length: 4528, dtype: int64
#dropped unnecessary rows
df.drop('description',axis =1, inplace =True)
df.head(2)
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in
0	s1	Movie	Dick Johnson Is Dead	Kirsten Johnson	NaN	United States	September 25, 2021	2020	PG-13	90 min	Documentaries
1	s2	TV Show	Blood & Water	NaN	Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...	South Africa	September 24, 2021	2021	TV-MA	2 Seasons	International TV Shows, TV Dramas, TV Mysteries
df.title.count()
8807
finding no. of movies and shows in data
df['type'].value_counts().plot(kind= 'bar', title = "No of Movies and show counts" , xlabel = "shows and Movies",
                              ylabel = 'Numbers' , color= 'Yellow', width = 0.2)
<Axes: title={'center': 'No of Movies and show counts'}, xlabel='shows and Movies', ylabel='Numbers'>

#it helps to find max no of releases in a year
df['release_year'].value_counts()
release_year
2018    1147
2017    1032
2019    1030
2020     953
2016     902
        ... 
1959       1
1925       1
1961       1
1947       1
1966       1
Name: count, Length: 74, dtype: int64
#finding the oldest movie or show in a netflix 
old = df['release_year'].min()

title = df[df['release_year']==old][['release_year','title']]
title
release_year	title
4250	1925	Pioneers: First Women Filmmakers*
#from here on trying to find the max number of genre
df['in_split']=df['listed_in'].str.split(', ')
df_exp= df.explode('in_split')
#finding the most popular genere
df_exp['in_split'].value_counts()
in_split
International Movies            2752
Dramas                          2427
Comedies                        1674
International TV Shows          1351
Documentaries                    869
                                ... 
TV Thrillers                      57
Movies                            57
Stand-Up Comedy & Talk Shows      56
Classic & Cult TV                 28
TV Shows                          16
Name: count, Length: 42, dtype: int64
#according to time period knowing the rise in movies and shows releases
a=df.groupby(['release_year','type']).size().unstack()
a.plot(kind='line',marker='*')
<Axes: xlabel='release_year'>

#visualizing the ratings of the movies and shows
b = df.groupby(['type','rating']).size().unstack()
b
/usr/local/lib/python3.11/dist-packages/pandas/io/formats/format.py:1458: RuntimeWarning: invalid value encountered in greater
  has_large_values = (abs_vals > 1e6).any()
/usr/local/lib/python3.11/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in less
  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()
/usr/local/lib/python3.11/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in greater
  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()
rating	66 min	74 min	84 min	G	NC-17	NR	PG	PG-13	R	TV-14	TV-G	TV-MA	TV-PG	TV-Y	TV-Y7	TV-Y7-FV	UR
type																	
Movie	1.0	1.0	1.0	41.0	3.0	75.0	287.0	490.0	797.0	1427.0	126.0	2062.0	540.0	131.0	139.0	5.0	3.0
TV Show	NaN	NaN	NaN	NaN	NaN	5.0	NaN	NaN	2.0	733.0	94.0	1145.0	323.0	176.0	195.0	1.0	NaN
b.plot(kind='bar')
<Axes: xlabel='type'>

Better Visualisation

b.plot(kind='bar', stacked=True, figsize=(10,6),width= 0.2)
<Axes: xlabel='type'>

df.head()
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	in_split
0	s1	Movie	Dick Johnson Is Dead	Kirsten Johnson	NaN	United States	September 25, 2021	2020	PG-13	90 min	Documentaries	[Documentaries]
1	s2	TV Show	Blood & Water	NaN	Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...	South Africa	September 24, 2021	2021	TV-MA	2 Seasons	International TV Shows, TV Dramas, TV Mysteries	[International TV Shows, TV Dramas, TV Mysteries]
2	s3	TV Show	Ganglands	Julien Leclercq	Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...	NaN	September 24, 2021	2021	TV-MA	1 Season	Crime TV Shows, International TV Shows, TV Act...	[Crime TV Shows, International TV Shows, TV Ac...
3	s4	TV Show	Jailbirds New Orleans	NaN	NaN	NaN	September 24, 2021	2021	TV-MA	1 Season	Docuseries, Reality TV	[Docuseries, Reality TV]
4	s5	TV Show	Kota Factory	NaN	Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...	India	September 24, 2021	2021	TV-MA	2 Seasons	International TV Shows, Romantic TV Shows, TV ...	[International TV Shows, Romantic TV Shows, TV...
Which month(s) see the most releases added to Netflix?
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.head(2)
show_id	type	title	director	cast	country	date_added	release_year	rating	duration	listed_in	in_split
0	s1	Movie	Dick Johnson Is Dead	Kirsten Johnson	NaN	United States	2021-09-25	2020	PG-13	90 min	Documentaries	[Documentaries]
1	s2	TV Show	Blood & Water	NaN	Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...	South Africa	2021-09-24	2021	TV-MA	2 Seasons	International TV Shows, TV Dramas, TV Mysteries	[International TV Shows, TV Dramas, TV Mysteries]
df['month_added']= df['date_added'].dt.month_name()
df['month_added'].value_counts()
month_added
July         819
December     797
September    765
April        759
October      755
August       749
March        734
January      727
June         724
November     697
May          626
February     557
Name: count, dtype: int64
#which country produces the most content 
df['country'].value_counts()
country
United States                             2818
India                                      972
United Kingdom                             419
Japan                                      245
South Korea                                199
                                          ... 
Romania, Bulgaria, Hungary                   1
Uruguay, Guatemala                           1
France, Senegal, Belgium                     1
Mexico, United States, Spain, Colombia       1
United Arab Emirates, Jordan                 1
Name: count, Length: 748, dtype: int64
#titles which are produced by india 
df.loc[df['country']=='India','title']
4                        Kota Factory
24                              Jeans
39                       Chhota Bheem
50                      Dharmakshetra
66      Raja Rasoi Aur Anya Kahaniyan
                    ...              
8773              Yanda Kartavya Aahe
8775                  Yeh Meri Family
8798                         Zed Plus
8799                            Zenda
8806                           Zubaan
Name: title, Length: 972, dtype: object
d=df.loc[df['rating'].isin(['TV-MA', 'PG-13']),'title'].count()
d
3697
#finding the number of releases each year
df['release_year'].value_counts().sort_index().plot(kind='line')
<Axes: xlabel='release_year'>

#finding top 10 countries by content count
df['country'].value_counts().head(10).plot(kind='bar')
<Axes: xlabel='country'>

sns.heatmap(pd.crosstab(df['type'],df['rating'] ),cmap='plasma')
<Axes: xlabel='rating', ylabel='type'>