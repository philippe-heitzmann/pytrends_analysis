from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

keyword_list=["donald trump"]
# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=keyword_list)

# Interest Over Time
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())

# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(f"related_queries_dict: {related_queries_dict}")

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df.head())

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head())

# Get Google Top Charts
top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
print(top_charts_df.head())

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword=keyword_list[0])
print(suggestions_dict)

# Get Google Realtime Search Trends
realtime_searches = pytrend.realtime_trending_searches(pn='IN')
print(realtime_searches.head())

# Recreate payload with multiple timeframes
pytrend.build_payload(kw_list=keyword_list, timeframe=['2024-09-04 2024-09-10', '2024-09-18 2024-09-24'])

# Multirange Interest Over Time
multirange_interest_over_time_df = pytrend.multirange_interest_over_time()
print(multirange_interest_over_time_df.head())