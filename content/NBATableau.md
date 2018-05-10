Title: NBA Tableau Dashboard
Slug: nba-dash
Date: 2018-05-10 17:00
Category: Tableau
Tags: Tableau, Dashboard, NBA, Basketball, SQL
author: Phil Bingham
Include: requirejs,jquery
Summary: An interactive Tableau Dashboard using data scraped from the NBA website and stored in an SQL database.
summaryimage: /images/nba.png, /images/tableau.jpg

Following on from my post [NBA Webscraping & Visualisation](https://hexhamallstar.github.io/nbaviz.html), in which I showed the structure and function of a webscraping app that gets data automatically from the official NBA website and stores it using an SQLite database, I decided that I wanted to create an interactive summary of players statistics over the season.

Tableau is a flexible piece of software used broadly for data analytics/business intelligence purposes, as it makes it easy to create visualisations that update as the data changes over time. Tableau does not natively support SQLite databases, however by downloading and installing the relevant ODBC drivers as seen on [this](https://onlinehelp.tableau.com/current/pro/desktop/en-us/odbc_customize.html) webpage.
The main components of my dashboard are:

* A chart that shows the top 5 players in terms of average per game of a statistic selected via a dropdown box. The dropdown box controls the value of a parameter which in turn controls the Measure used to aggregate via CASE statements.
* A web container, which is directed to a URL defined by the player that has been clicked on in the first chart. This URL points to an image of the player, and is controlled by a URL action.
* A text table containing the most important statistics for the selected player. This is controlled by a filter action.

The final result is a clean dashboard that allows the user to explore statistics they are interested in and see the top players in each category, as well as see an individual summary on click.

<body>
<div class='tableauPlaceholder' id='viz1525971669728' style='position: relative'><noscript><a href='#'><img alt='NBA 2017&#47;18 Regular Season Per-Game Stat LeadersUse the drop-down menu on the right to choose a statisticClick on a bar to get that players regular season summary ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NB&#47;NBASeasonStatsStory&#47;StatLeadersDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NBASeasonStatsStory&#47;StatLeadersDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NB&#47;NBASeasonStatsStory&#47;StatLeadersDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1525971669728');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='650px';vizElement.style.height='887px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
</body>
