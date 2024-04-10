import streamlit as st
import pandas as pd
from annotated_text import annotated_text
import matplotlib.pyplot as plt



# import st_annotated_text

portfolio_1_df = pd.read_csv("portfolio1-2.csv")

#for each of the suggestions from the advisor, we want a titel taht says what they should do, then a dropdown with all details in a table and the rationale with links attached
#then an option to say yes, no, let's dicusss

#Give an overview of what those changes would look like in terms of total portfolio value from there

# st.dataframe(portfolio_1_df)

st.markdown("##### Welcome Back, Stuart")
st.header("Suggestions")

for index, row in portfolio_1_df.iterrows():
    feed_ticker = row['Stock Code']
    feed_action = row['Action']
    feed_curr_alloc = row['Current Portfolio Allocation']
    feed_recc_alloc = row['Recommended Portfolio Allocation']
    feed_dv = row['Dollar Value']
    feed_rationale = row['Rationale']
    feed_prompt = ''

    feed_dv = feed_dv.replace("(", "").replace(")", "")

    #initial tickers at front of textbox
    # if feed_action == 'Buy up to Benchmark':
    #     feed_prompt = f" :green[{feed_action}]"
    # else:
    #     feed_prompt = f" :red[{feed_action}]"

    #Have different formats for a buy and a sell product

    expander_text = ''
    if feed_action == 'Buy up to Benchmark':
        expander_text = f"`{feed_ticker}` `{feed_action}`  You should buy up to the benchmark of {feed_ticker} for {feed_dv}"
    else:
        expander_text = f"`{feed_ticker}` `{feed_action}`  You should sell {feed_ticker} down to the benchmark of {feed_recc_alloc} at a value of {feed_dv}"


    #formatting the table to be displayed
    feed_table = portfolio_1_df.iloc[index, 0:5]
    feed_table_df = feed_table.to_frame().reset_index(inplace = False)
    feed_table_df.rename(columns={feed_table_df.columns[0]: ' ',feed_table_df.columns[1]: 'Information'}, inplace=True)
    # feed_table_df = feed_table_df.reset_index().drop('level_0')
    print(feed_table_df.columns)


    with st.expander(expander_text):
        col1, col2 = st.columns(2)

        # Add content to the first column
        with col1:
            st.table(feed_table_df)

        # Add content to the second column
        with col2:
            st.markdown("##### Rationale:")
            st.write(feed_rationale)

            st.markdown("###### Relevant links :")
            st.markdown("https://www.wilsonsadvisory.com.au/news/telstra-a-defensive-business-with-an-impr")
        feed_feedback = st.radio(
                    "What do you think about this action?",
                    ["Agree", "Disagree", "Need to discuss"],
                    index=None, 
                    key=f"feed_feedback_{index}", 
                    horizontal=True, 
                )



###Demo charts example
labels = 'TLS', 'MFG', 'RMD', 'ASB'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels_2 = 'MFG', 'RMD', 'ASB', 'WDS'
sizes_2 = [30, 45, 10, 15]
explode_2 = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig2, ax2 = plt.subplots()
ax2.pie(sizes_2, explode=explode_2, labels=labels_2, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


col1, col2 = st.columns(2)
    # Add content to the first column
with col1:
    st.markdown("##### Current Portfolio:")
    st.pyplot(fig1)

    # Add content to the second column
with col2:
    st.markdown("##### Recommended Portfolio:")
    st.pyplot(fig2)



