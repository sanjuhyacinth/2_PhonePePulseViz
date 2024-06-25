# Library imports:
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objs as go
import mysql.connector

# MySQL connection:
conn = mysql.connector.connect(
        host="hostname",
        user="root",
        password="password",
        database="dbname"
    )
mycursor = conn.cursor()

# set up page configuration for streamlit
icon = 'https://images.app.goo.gl/DPGYgZvry2fdrbog6'
st.set_page_config(page_title='PHONEPE PULSE',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide',menu_items={"about":'This streamlit application was developed by Sanju'})

title_text = '''<h1 style='font-size: 36px;color:violet;text-align: center;'>PHONEPE PULSE: The Heartbeat of India's Digital Revolution</h1>'''
st.markdown(title_text, unsafe_allow_html=True)

#set up home page and optionmenu 
selected = option_menu(None,
                        options=["HOME", "TOP VISUALS", "TOP INSIGHTS", "ABOUT"],
                        icons=["house-fill", "globe-central-south-asia", "lightbulb", "info-circle-fill"],
                        default_index=0,
                        orientation="horizontal",
                        styles={"container": {"width": "100%","border": "2px ridge #000000","background-color": "#50277C"},
                                "icon": {"color": "#F4F0FE", "font-size": "20px"}})

#setup the detail for the option 'HOME'
if selected == "ABOUT":
        st.subheader(":violet[Project Title :]")
        st.markdown("Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly",unsafe_allow_html=True)
        st.subheader(":violet[Domain :]")
        st.markdown("Fintech")
        st.subheader(":violet[Skills Employed :]")
        st.markdown("Github Cloning, Python, Pandas, MySQL, Streamlit and Plotly.",unsafe_allow_html=True)
        st.subheader(":violet[Overview :]")
        st.markdown('''##### In this project, we aim to use hte :violet[Phonepe Pulse data] from Github and Visualise it on the streamlit app using the plotly library in python.''')
        st.write('')
        st.markdown('''
                    :red[Git:] Employed Git for version control and efficient collaboration, enabling seamless cloning of the PhonePe dataset from GitHub.<p>
                    :red[Pandas:] Leveraged the powerful Pandas library to transform the dataset from JSON format into a structured dataframe. Pandas facilitated data manipulation, cleaning, and preprocessing, ensuring the data was ready for analysis.<p>
                    :red[MySQL Connector:] Utilized MySQL Connector to establish a connection to MySQL database, enabling seamless integration of the transformed dataset and the data was efficiently inserted into relevant tables for storage and retrieval.<p>
                    :red[Streamlit:] Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.<p>
                    :red[Plotly:] Integrated Plotly, a versatile plotting library, to generate insightful visualizations from the dataset. Plotly's interactive plots, including geospatial plots and other data visualizations, provided users with a comprehensive understanding of the dataset's contents.''',unsafe_allow_html=True)
        st.subheader(':violet[Contact :]')
        st.markdown('##### Linkedin: www.linkedin.com/in/sanju-hyacinth/')
        st.markdown('##### GitHub : https://github.com/sanjuhyacinth')


#setup the detail for the option 'ABOUT'
if selected =="HOME":
        c1,c2=st.columns([1.5,1],gap="large")
        with c1:
                st.subheader(':violet[What is Phonepe?]')
                st.markdown('''PhonePe is a popular digital payments platform in India, offering a range of financial services through its mobile app.
                            Users can make payments, transfer money, recharge phones, pay bills, invest, shop online, and more.<p>
                            PhonePe has easily become a preferred choice of payment app for millions of users, contributing to India's digital payments revolution.''',unsafe_allow_html=True)
                
                st.markdown("##### :violet[Learn more about PhonePe's journey by clicking the button below!]")
                st.link_button("PhonePe - About us", "https://www.phonepe.com/about-us/")
        with c2:  
                st.write(' ')    
                st.markdown("![Alt Text](https://1.bp.blogspot.com/-w5bZ0nrUWF8/XmMlpd94X7I/AAAAAAAAAaU/qnZx23SsovkwMfxv8O8n3cgdkH3OWOSygCLcBGAsYHQ/s400/1_E8Ys7gfVryzMjtpYy9Z6gw.gif)")          
               
        c1,c2=st.columns([2,1],gap="large")
        with c1:
                st.subheader(':violet[What is Phonepe Pulse?]')
                st.markdown('''PhonePe Pulse provides :violet[**real-time insights and trends on digital payments**] across India.
                It offers comprehensive analytics which includes transaction volumes, consumer demographics, popular merchant categories,
                geographic trends, transaction values, payment methods, and seasonal fluctuations.''',unsafe_allow_html=True)
        
        with c2:   
                st.write(' ')             
                st.markdown("![Alt Text](https://www.phonepe.com/pulsestatic/pulse/static/pulse-a7eb70ef6c6c2c5a9d1b3c3fd66752f5.gif)")
        
        c1,c2=st.columns([1.5,2], gap = "small")
        
        with c1:
                st.write(' ')
                st.image('https://www.phonepe.com/pulsestatic/791/pulse/static/4cb2e7589c30e73dca3d569aea9ca280/1b2a8/pulse-2.webp',use_column_width=True)
                
        with c2:
                st.subheader(':violet[PhonePe Pulse - What Insights does it provide?]')
                st.markdown("#### :violet[Transactions :]")
                st.markdown('''
                        Transaction insights involve analyzing customer transaction data to understand behavior and preferences.
                        By examining trends, categorizing transactions,and identifying patterns of India.''',unsafe_allow_html=True)
                st.markdown("#### :violet[Users :]")
                st.markdown('''
                        User insights refer to analyzing customer demographics, engagement metrics, and feedback.
                        By understanding demographics, tracking engagement of user in India ''',unsafe_allow_html=True)
                
                st.markdown("##### :violet[This project is inspired by PhonePe Pulse :]")
                st.link_button('Phonepe Pulse - The beat of progress','https://www.phonepe.com/pulse/')

#setup details for the option "Geo Visualization"
if selected =="TOP VISUALS":
        
        def ind_geo():
                geo="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                return geo
        inside_pages = option_menu(None,
                        options=["GEO VISUALIZATIONS", "OTHER VISUALIZATIONS"],
                        icons=["globe-central-south-asia", "bar-chart-fill"],
                        default_index=0,
                        orientation="horizontal")
        
        if inside_pages == "GEO VISUALIZATIONS":
                st.write(' ')
                st.info(
                """
                In this section, we are constructing :red[geo visualizations] by displaying the transaction and user data State-wise, which can
                be aggregated either as a whole or can be partitioned/filtered by Year and Quarter.             
                """)
        
                geo_type = st.selectbox('Category Selection',["Transactions","Users"], index = None)
                st.write("Selection made :", f"<span style='color:#E982FA'>{geo_type}</span>", unsafe_allow_html=True)

                if geo_type=="Transactions":
                        cat= st.selectbox('Transaction Selection',["Transaction Amount","Transaction Count"], index = None)
                        st.write("Selection made :", f"<span style='color:#E982FA'>{cat}</span>", unsafe_allow_html=True)
                        if cat == "Transaction Amount":
                                agg_type_list = ['Overall aggregation','Time Filters']
                                agg_type = st.radio("Choose Aggregation", agg_type_list, index = None)

                                if agg_type == "Overall aggregation":                       
                                        st.title(":violet[ Overall State-wise Total Transaction Amount ]")
                                        mycursor.execute('''SELECT State, round(sum(Transaction_amount),2) as 'Total Transaction Amount',
                                                round(AVG(Transaction_amount),2) as 'Average Transaction Amount'
                                                from agg_trans
                                                GROUP BY State''')
                                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Transaction Amount','Average Transaction Amount'])
                                        
                                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='State',
                                                hover_data=['Total Transaction Amount','Average Transaction Amount'],
                                                color='Total Transaction Amount',
                                                color_continuous_scale=px.colors.sequential.Burg,
                                                mapbox_style="carto-positron",zoom=3,
                                                center={"lat": 21.7679, "lon": 78.8718},)

                                        fig.update_geos(fitbounds="locations", visible=False)
                                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                        fig.update_layout(height=450)
                                        st.plotly_chart(fig,use_container_width = True)
                                        st.write(' ')
                                        st.write(' ')
                                        st.subheader(":violet[Tabular view of visual]")
                                        st.dataframe(df)
                                
                                if agg_type == "Time Filters":
                                        c1,c2 = st.columns([1.5, 1], gap = "small")
                                        with c1:
                                                mycursor.execute(f"SELECT DISTINCT Year as 'Year' from agg_trans")
                                                df_y = pd.DataFrame(mycursor.fetchall(), columns=['Year'])
                                                y_slider = st.select_slider("Year",options=df_y['Year'].tolist())
                                        with c2:
                                                mycursor.execute(f"SELECT DISTINCT Quarter as 'Quarter' from agg_trans")
                                                df_q = pd.DataFrame(mycursor.fetchall(), columns=['Quarter'])
                                                q_slider = st.select_slider("Quarter",options=df_q['Quarter'].tolist())
                                        
                                        mycursor.execute(f"SELECT State, round(sum(Transaction_amount),2) as 'Total Transaction Amount', round(AVG(Transaction_amount),2) as 'Average Transaction Amount' FROM agg_trans where Year = {y_slider} and Quarter = {q_slider} GROUP BY State")
                                        df = pd.DataFrame(mycursor.fetchall(), columns=['State','Total Transaction Amount','Average Transaction Amount'])
                                        
                                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='State',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale=px.colors.sequential.BuGn,
                                        mapbox_style="carto-positron",zoom=3,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                        fig.update_geos(fitbounds="locations", visible=False)
                                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                        fig.update_layout(height=475)
                                        st.subheader(f":violet[Total Transaction Amount for States in {y_slider} for Q{q_slider} ]")
                                        st.plotly_chart(fig,use_container_width = True)

                                        st.write(' ')
                                        st.subheader(":violet[Tabular view of visual]")
                                        st.dataframe(df)
                                                
                        if cat =="Transaction Count":
                                agg_type_list = ['Overall aggregation','Time Filters']
                                agg_type = st.radio("Choose Aggregation", agg_type_list, index = None)

                                if agg_type == 'Overall aggregation':
                                        st.title(":violet[ Overall State-wise Total Transaction Count ]")
                                        mycursor.execute('''SELECT State, round(sum(Transaction_count),2) as 'Total Transaction Count',
                                                round(AVG(Transaction_count),2) as 'Average Transaction Count'
                                                from agg_trans
                                                GROUP by State''')
                                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Transaction Count','Average Transaction Count'])
                                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='State',
                                                hover_data=['Total Transaction Count','Average Transaction Count'],
                                                color='Total Transaction Count',
                                                color_discrete_sequence=px.colors.sequential.Burg,
                                                mapbox_style="carto-positron",zoom=3,
                                                center={"lat": 21.7679, "lon": 78.8718},)

                                        fig.update_geos(fitbounds="locations", visible=False)
                                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                        fig.update_layout(height=450)
                                        st.plotly_chart(fig,use_container_width = True)
                                        st.write(' ')
                                        st.write(' ')
                                        st.subheader(":violet[Tabular view of visual]")
                                        st.dataframe(df)

                                if agg_type == "Time Filters":
                                        c1,c2 = st.columns([1.5, 1], gap = "small")
                                        with c1:
                                                mycursor.execute(f"SELECT DISTINCT Year as 'Year' from agg_trans")
                                                df_y = pd.DataFrame(mycursor.fetchall(), columns=['Year'])
                                                y_slider = st.select_slider("Year",options=df_y['Year'].tolist())
                                        with c2:
                                                mycursor.execute(f"SELECT DISTINCT Quarter as 'Quarter' from agg_trans")
                                                df_q = pd.DataFrame(mycursor.fetchall(), columns=['Quarter'])
                                                q_slider = st.select_slider("Quarter",options=df_q['Quarter'].tolist())
                                        
                                        mycursor.execute(f"SELECT State, round(sum(Transaction_count),2) as 'Total Transaction Count', round(AVG(Transaction_count),2) as 'Average Transaction Count' FROM agg_trans where Year = {y_slider} and Quarter = {q_slider} GROUP BY State")
                                        df = pd.DataFrame(mycursor.fetchall(), columns=['State','Total Transaction Count','Average Transaction Count'])
                                        
                                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='State',
                                        hover_data=['Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Count',
                                        color_discrete_sequence=px.colors.sequential.Burg,
                                        mapbox_style="carto-positron",zoom=3,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                        fig.update_geos(fitbounds="locations", visible=False)
                                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                        fig.update_layout(height=475)
                                        st.subheader(f":violet[Total Transaction Count of States in {y_slider} for Q{q_slider} ]")
                                        st.plotly_chart(fig,use_container_width = True)

                                        st.write(' ')
                                        st.subheader(":violet[Tabular view of visual]")
                                        st.dataframe(df)

                if geo_type=="Users":
                        cat1= st.selectbox('User Aggregation',["Registered Users","App Opens"], index = None)
                        st.write("Selection made :", f"<span style='color:#E982FA'>{cat1}</span>", unsafe_allow_html=True)
                        if cat1 == "Registered Users":
                                cat_type_list = ['Overall aggregation','Time Filters']
                                cat_type = st.radio("Choose Aggregation", cat_type_list, index = None)

                                if cat_type == 'Overall aggregation':
                                        st.title(" :violet[ Overall State-wise Total Registered Users] ")

                                        c1,c2 = st.columns([1,2], gap="small")
                                        with c1:
                                                mycursor.execute('''SELECT State, round(sum(User_count),2) as 'Total Users'
                                                                from agg_user
                                                                GROUP BY State''')
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Users'])
                                                st.subheader(" :grey[ Tabular Visualization] ")
                                                st.write(' ')
                                                st.dataframe(df)
                                        with c2:
                                                st.subheader(":grey[ Geographical Visualization]")
                                                st.write(' ')
                                                mycursor.execute('''SELECT State, round(sum(User_count),2) as 'Total Users'
                                                        from agg_user
                                                        GROUP BY State''')
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Users'])
                                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                        locations='State',
                                                        hover_data=['Total Users'],
                                                        color='Total Users',
                                                        color_discrete_sequence=px.colors.sequential.Purp,
                                                        mapbox_style="carto-positron",zoom=2.5,
                                                        center={"lat": 21.7679, "lon": 78.8718},)

                                                fig.update_geos(fitbounds="locations", visible=False)
                                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                                fig.update_layout(height=400)
                                                st.plotly_chart(fig,use_container_width = True)
                                        
                                if cat_type == "Time Filters":
                                        c1,c2 = st.columns([1.5, 1], gap = "small")
                                        with c1:
                                                mycursor.execute(f"SELECT DISTINCT Year as 'Year' from agg_user")
                                                df_year = pd.DataFrame(mycursor.fetchall(), columns=['Year'])
                                                slider_y = st.select_slider("Year",options=df_year['Year'].tolist())
                                        with c2:
                                                mycursor.execute(f"SELECT DISTINCT Quarter as 'Quarter' from agg_user")
                                                df_quart = pd.DataFrame(mycursor.fetchall(), columns=['Quarter'])
                                                slider_q = st.select_slider("Quarter",options=df_quart['Quarter'].tolist())
                                        
                                        st.title(f":violet[Total Users by States in {slider_y} for Q{slider_q} ]")
                                        st.write(' ')
                                        c1,c2 = st.columns([1,1.5], gap="small")
                                        with c1:
                                                mycursor.execute(f"SELECT State, round(sum(User_count),2) as 'Total Users' from agg_user where Year = {slider_y} and Quarter = {slider_q} GROUP BY State")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Users'])
                                                st.subheader(" :grey[ Tabular Visualization] ")
                                                st.write(' ')
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"SELECT State, round(sum(User_count),2) as 'Total Users' from agg_user where Year = {slider_y} and Quarter = {slider_q} GROUP BY State")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Users'])
                                                st.subheader(f":grey[Geographical Visualization - {slider_y} for Q{slider_q} ]")
                                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='State',
                                                hover_data=['Total Users'],
                                                color='Total Users',
                                                color_discrete_sequence=px.colors.sequential.Purp,
                                                mapbox_style="carto-positron",zoom=3,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                                fig.update_geos(fitbounds="locations", visible=False)
                                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                                fig.update_layout(height=475)
                                                st.plotly_chart(fig,use_container_width = True)

                        if cat1 == "App Opens":
                                cat_type_list = ['Overall aggregation','Time Filters']
                                cat_type = st.radio("Choose Aggregation", cat_type_list, index = None)

                                if cat_type == 'Overall aggregation':
                                        st.title(" :violet[ Overall State-wise App Opens] ")
                                        c1,c2 = st.columns([1,2], gap="small")

                                        with c1:
                                                mycursor.execute('''SELECT State, round(sum(App_opens),2) as 'Total App Opens'
                                                        from map_user
                                                        GROUP BY State''')
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total App Opens'])
                                                st.subheader(" :grey[ Tabular Visualization] ")
                                                st.write(' ')
                                                st.dataframe(df)
                                        
                                        with c2:
                                                st.subheader(":grey[ Geographical Visualization]")
                                                st.write(' ')
                                                mycursor.execute('''SELECT State, round(sum(App_opens),2) as 'Total App Opens'
                                                        from map_user
                                                        GROUP BY State''')
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total App Opens'])
                                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                        locations='State',
                                                        hover_data=['Total App Opens'],
                                                        color='Total App Opens',
                                                        color_discrete_sequence=px.colors.sequential.Purp,
                                                        mapbox_style="carto-positron",zoom=3,
                                                        center={"lat": 21.7679, "lon": 78.8718},)

                                                fig.update_geos(fitbounds="locations", visible=False)
                                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                                fig.update_layout(height=450)
                                                st.plotly_chart(fig,use_container_width = True)
                                
                                if cat_type == "Time Filters":

                                        c1,c2 = st.columns([1.5, 1], gap = "small")
                                        with c1:
                                                mycursor.execute(f"SELECT DISTINCT Year as 'Year' from map_user")
                                                df_year = pd.DataFrame(mycursor.fetchall(), columns=['Year'])
                                                slider_y = st.select_slider("Year",options=df_year['Year'].tolist())
                                        with c2:
                                                mycursor.execute(f"SELECT DISTINCT Quarter as 'Quarter' from map_user")
                                                df_quart = pd.DataFrame(mycursor.fetchall(), columns=['Quarter'])
                                                slider_q = st.select_slider("Quarter",options=df_quart['Quarter'].tolist())
                                        
                                        st.title(f":violet[Total App Opens by States in {slider_y} for Q{slider_q} ]")
                                        st.write(' ')
                                        c1,c2 = st.columns([1,1.5], gap="small")
                                        with c1:
                                                mycursor.execute(f"SELECT State, round(sum(App_Opens),2) as 'Total App Opens' from map_user where Year = {slider_y} and Quarter = {slider_q} GROUP BY State")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total App Opens'])
                                                st.subheader(" :grey[ Tabular Visualization] ")
                                                st.write(' ')
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"SELECT State, round(sum(App_Opens),2) as 'Total App Opens' from map_user where Year = {slider_y} and Quarter = {slider_q} GROUP BY State")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total App Opens'])
                                                st.subheader(f":grey[Geographical Visualization - {slider_y} for Q{slider_q} ]")
                                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='State',
                                                hover_data=['Total App Opens'],
                                                color='Total App Opens',
                                                color_discrete_sequence=px.colors.sequential.Burg,
                                                mapbox_style="carto-positron",zoom=3,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                                fig.update_geos(fitbounds="locations", visible=False)
                                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                                fig.update_layout(height=475)
                                                st.plotly_chart(fig,use_container_width = True)


        if inside_pages == "OTHER VISUALIZATIONS":
                st.write(' ')
                st.info(
                """
                In this section, we are going to make use of data filters, specifically the :red[States] so that we can see a few aggregations which are not covered in the geo visuals.
                We have covered a bunch of questions here. Toggle the filter option to proceed.              
                """)
                go_button = st.toggle(" Open State Filters ")

                if go_button:
                        viz_list = st.selectbox('Visualization list',[
                                        "District-wise aggregation of transaction",
                                        "Year wise amount and count aggregation for all quarters",
                                        "Transaction amount and count by the type of transaction",
                                        "User Counts by Phone Brands",
                                        "District-wise Total User Counts"],
                                        index = None)
                        
                        if viz_list == 'District-wise aggregation of transaction':
                                mycursor.execute("Select distinct State as 'State' from map_trans")
                                df_states = pd.DataFrame(mycursor.fetchall(), columns=['State'])
                                state_select = st.selectbox("States ", options = df_states['State'].tolist(), index = None)

                                if state_select:
                                        st.title(':violet[ District-wise aggregation of transaction ]')
                                        st.markdown(''' The district wise split of Transaction amount and count is displayed in the form of a 
                                                    data table and bar chart. The bar chart has :violet[District] on the x axis and :violet[Transaction amount] 
                                                    on the y axis, coloured based on :violet[Total Transaction Amount] basis districts. We can see the table and chart
                                                    updating with every change in the State filter.''') 
                                        st.write(' ')
                                        c1,c2 = st.columns([1.5,2], gap = "small")
                                        with c1:
                                                st.subheader(":grey[ Tabular view of Data ]")
                                                st.write(' ')
                                                mycursor.execute(f"select District, round(sum(Transaction_amount),2) as 'Total Amount', round(sum(Transaction_count),2) as 'Total Count' from map_trans where State = '{state_select}' group by District;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['District','Total Amount','Total Count']).reset_index(drop=True)
                                                df.index += 1
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"select District, round(sum(Transaction_amount),2) as 'Total Amount', round(sum(Transaction_count),2) as 'Total Count' from map_trans where State = '{state_select}' group by District;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['District','Total Amount','Total Count'])
                                                st.subheader(":grey[ Graphical View of Data ]")
                                                fig = px.bar(df, x= 'District', y = 'Total Amount',
                                                orientation='v',
                                                color='Total Amount',
                                                hover_data= ['Total Count'], 
                                                color_continuous_scale=px.colors.sequential.Sunset,
                                                labels= None)
                                                fig.update_layout(showlegend=False)
                                                st.plotly_chart(fig,use_container_width=True)

                        elif viz_list == 'Year wise amount and count aggregation for all quarters':
                                mycursor.execute("Select distinct State as 'State' from agg_trans")
                                df_states = pd.DataFrame(mycursor.fetchall(), columns=['State'])
                                state_select = st.selectbox("States ", options = df_states['State'].tolist(), index = None)

                                if state_select:
                                        st.title(':violet[ Year-wise Transaction Amount and Count Aggregation ]')
                                        st.markdown("###### :violet[ * Includes all quarters in a year]")
                                        st.markdown(''' The Year-wise split of Transaction amount and count is displayed in the form of a 
                                                    data table and bar chart. The bar chart has :violet[Total Transaction amount] on the x axis and
                                                    :violet[Year] on the y axis, coloured based on the :violet[Total Transaction amount]. We can see the table and chart
                                                    updating with every change in the State filter.''') 
                                        st.write(' ')
                                        c1,c2 = st.columns([1.5,2], gap = "small")
                                        with c1:
                                                st.subheader(":grey[ Tabular view of Data ]")
                                                st.write(' ')
                                                mycursor.execute(f"select Year, round(sum(Transaction_amount),2) as 'Total Amount', round(sum(Transaction_count),2) as 'Total Count' from agg_trans where State = '{state_select}' group by Year;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Year','Total Amount','Total Count']).reset_index(drop=True)
                                                df.index += 1
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"select Year, round(sum(Transaction_amount),2) as 'Total Amount', round(sum(Transaction_count),2) as 'Total Count' from agg_trans where State = '{state_select}' group by Year;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Year','Total Amount','Total Count'])
                                                st.subheader(":grey[ Graphical View of Data ]")
                                                fig = px.bar(df, x= 'Total Amount', y = 'Year',
                                                orientation='h',
                                                color='Total Amount',
                                                hover_data= ['Total Count'],       
                                                color_continuous_scale=px.colors.sequential.Burg_r,
                                                labels= None)
                                                fig.update_layout(showlegend=True)
                                                st.plotly_chart(fig,use_container_width=True)
                        
                        elif viz_list == 'Transaction amount and count by the type of transaction':
                                mycursor.execute("Select distinct State as 'State' from agg_trans")
                                df_states = pd.DataFrame(mycursor.fetchall(), columns=['State'])
                                state_select = st.selectbox("States ", options = df_states['State'].tolist(), index = None)

                                if state_select:
                                        st.title(':violet[ Year-wise Transaction Amount and Count Split by Transaction Type]')
                                        st.markdown("###### :violet[ * Includes all quarters in a year]")
                                        st.markdown(''' The Year-wise split of Transaction amount and count by Transaction Type shows the categories where the payments have flowed in these years.
                                                    The data is displayed in the form of a table and stacked bar chart, having :violet[Total Transaction amount] on the x axis and
                                                    :violet[Year] on the y axis, coloured based on the :violet[Transaction Type] category. We can see the table and chart
                                                    updating with every change in the State filter.''') 
                                        st.write(' ')
                                        c1,c2 = st.columns([1.5,2], gap = "small")
                                        with c1:
                                                st.subheader(":grey[ Tabular view of Data ]")
                                                st.write(' ')
                                                mycursor.execute(f"select Year, Transaction_type as 'Tran Type', round(sum(Transaction_amount),2) as 'Total Amount',  round(sum(Transaction_count),2) as 'Total Count'  from agg_trans where State = '{state_select}' group by Transaction_type, Year;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Year','Tran Type','Total Amount','Total Count']).reset_index(drop=True)
                                                df.index += 1
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"select Year, Transaction_type as 'Tran Type', round(sum(Transaction_amount),2) as 'Total Amount',  round(sum(Transaction_count),2) as 'Total Count'  from agg_trans where State = '{state_select}' group by Transaction_type, Year;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Year','Tran Type','Total Amount','Total Count'])
                                                st.subheader(":grey[ Graphical View of Data ]")
                                                fig = px.bar(df, x = 'Total Amount', y= 'Year',
                                                orientation='h',
                                                color='Tran Type',
                                                hover_data= ['Total Count'],       
                                                #color_continuous_scale=px.colors.sequential.Purples,
                                                labels= None)
                                                fig.update_layout(showlegend=True)
                                                st.plotly_chart(fig,use_container_width=True)

                        elif viz_list == 'User Counts by Phone Brands':
                                mycursor.execute("Select distinct State as 'State' from agg_user")
                                df_states = pd.DataFrame(mycursor.fetchall(), columns=['State'])
                                state_select = st.selectbox("States ", options = df_states['State'].tolist(), index = None)

                                if state_select:
                                        st.title(':violet[ State-wise App User Counts by Phone Brands]')
                                        st.markdown("###### :violet[ * Aggregation includes all years]")
                                        st.markdown(''' This is a State-wise split of the App User Counts by the Brand of Phones used by customers.
                                                    The data is displayed in the form of a table and donut chart, having :violet[App User Counts] as the values segmented
                                                    by :violet[phone Brands] as categories. We can see the table and chart updating with every change in the State filter.''') 
                                        st.write(' ')
                                        c1,c2 = st.columns([1.5,2], gap = "small")
                                        with c1:
                                                st.subheader(":grey[ Tabular view of Data ]")
                                                st.write(' ')
                                                mycursor.execute(f"select Brands, sum(User_count) as 'User Count', round(avg(User_percentage)*100,2) as 'Average %' from agg_user where State = '{state_select}' group by State, Brands order by 'User count' desc;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Brands','User Count','Average %']).reset_index(drop=True)
                                                df.index += 1
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"select Brands, sum(User_count) as 'User Count', round(avg(User_percentage)*100,2) as 'Average %' from agg_user where State = '{state_select}' group by State, Brands order by 'User count' desc;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['Brands','User Count','Average %'])
                                                st.subheader(":grey[ Graphical View of Data ]")
                                                fig = px.pie(df, values='User Count', names='Brands',
                                                color_discrete_sequence=px.colors.sequential.Sunsetdark,
                                                hover_data=['Average %'],
                                                labels={'User_count':'User Count'},
                                                hole = 0.45,
                                                opacity=0.9)
                                                fig.update_traces(textposition='inside', textinfo='percent+label')
                                                fig.update_layout(showlegend=True)
                                                st.plotly_chart(fig,use_container_width=True)

                        else:
                                mycursor.execute("Select distinct State as 'State' from map_user")
                                df_states = pd.DataFrame(mycursor.fetchall(), columns=['State'])
                                state_select = st.selectbox("States ", options = df_states['State'].tolist(), index = None)

                                if state_select:
                                        st.title(':violet[ District-wise Total App User Counts and Open Counts]')
                                        st.markdown("###### :violet[ * Aggregation includes all years and quarters]")
                                        st.markdown(''' This is a District-wise split of Total App Users and Opens over all the years. The data is displayed in the form of a 
                                                    table and bar chart, having :violet[Districts] on the x axis and :violet[Total App Opens] on the y axis, also displaying the 
                                                    :violet[Total App User Counts] while hovering over the bars. We can see the table and chart updating with every change in the State filter.''') 
                                        st.write(' ')
                                        c1,c2 = st.columns([1.5,2], gap = "small")
                                        with c1:
                                                st.subheader(":grey[ Tabular view of Data ]")
                                                st.write(' ')
                                                mycursor.execute(f"select District, sum(Registered_users) as 'Total Users', sum(App_Opens) as 'Total App Opens' from map_user where State = '{state_select}' group by District;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['District','Total Users','Total App Opens']).reset_index(drop=True)
                                                df.index += 1
                                                st.dataframe(df)
                                        with c2:
                                                mycursor.execute(f"select District, sum(Registered_users) as 'Total Users', sum(App_Opens) as 'Total App Opens' from map_user where State = '{state_select}' group by District;")
                                                df = pd.DataFrame(mycursor.fetchall(), columns=['District','Total Users','Total App Opens'])
                                                st.subheader(":grey[ Graphical View of Data ]")
                                                fig = px.bar(df, x = 'District', y= 'Total App Opens',
                                                orientation='v',
                                                hover_data= ['Total Users'],       
                                                color_continuous_scale=px.colors.sequential.Agsunset,
                                                labels= {'App_Opens':'Total App Opens'})
                                                fig.update_layout(showlegend=True)
                                                st.plotly_chart(fig,use_container_width=True)
                                                
#setup details for the option "TOP INSIGHTS"
if selected =="TOP INSIGHTS":
        st.info(
                """
                ##### What does the Top Insights section display:
                In this section, we are going to be visualising a few questions, mostly the "Top 10s" 
                to gain better understanding and visual representation of the data made available by Phonepe.
                """)
        
        qns = st.selectbox("**Questions**", (
                "1. Top 10 States: Highest and Lowest Transaction Amounts (with counts)", 
                "2. Top 10 Districts: Highest and Lowest Transaction Amounts (with counts)",
                "3. Top 10 Pincodes: Highest and Lowest Transaction Amounts (with counts)",
                "4. Top State: Highest and Lowest performing State annually based on Transaction Amount ",
                "5. Top Types: Highest Transaction Types by Transactions",
                "6. Top 10 States: Highest and Lowest User counts",
                "7. Top 10 Mobile Brands: Highest and Lowest User counts",
                "8. Top 10 Districts: Highest and Lowest App Opens",
                "9. Top 10 Pincodes: Highest and Lowest Registered Users", 
                "10. Top District: Highest and Lowest performing District annually by User Counts"),
                index=None
                )

        # Top Insights - Questions    
        if qns == "1. Top 10 States: Highest and Lowest Transaction Amounts (with counts)":
                st.title(":violet[Top 10 States : Highest & Lowest Transactions]")
                st.write('')
                col1,col2 = st.columns([1.5,1.8],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Transaction Amount and Counts - States]")
                        mycursor.execute('''SELECT State, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM agg_trans GROUP BY State 
                                         ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Amount', 'Total Count'])
                        fig = px.bar(df, x= 'Total Amount', y = 'State', orientation='h', 
                                     color = 'Total Amount',
                                     color_continuous_scale=px.colors.sequential.Greens,
                                     hover_data=['Total Count'],
                                     labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest Transaction Amount and Counts - States]")
                        st.write(' ')
                        mycursor.execute('''SELECT State, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM agg_trans GROUP BY State 
                                         ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Amount', 'Total Count'])
                        fig = px.bar(df, x= 'Total Amount', y = 'State', orientation='h', 
                                     color = 'Total Amount',
                                     color_continuous_scale=px.colors.sequential.Burg,
                                     hover_data=['Total Count'],
                                     labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="small")
                with c1:
                        st.subheader(":violet[Highest Transaction States - Table]")
                        mycursor.execute('''SELECT State, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM agg_trans GROUP BY State 
                                         ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Amount', 'Total Count']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[Telangana] leads the list in being the top state with highest transaction amount amounting to
                                            **30.7 Trillion worth of transactions**, followed closely by :violet[Maharashtra] on the 2nd with 
                                            roughly **29 Trillion** and :violet[Karnataka] with **28.8 Trillion** worth of transactions. 
                                            - The top 3 States are :violet[_technologically advanced_] areas of the country seeing a lot of digital transactions on a day-to-day basis,
                                            leading to their prominence in the app.
                                            - Maharashtra, being the financial capital of the country has without doubt seen itself on the top of the transaction counts list.
                                            - Telangana is on the top even with less than approx 4 billion number of transactions in comparison to Maharashtra
                                            giving a picture of :violet[more high value transactions with the app]. A similar kind of pattern is observed with Andhra Pradesh on the 4th place.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Transaction States - Table]")
                       mycursor.execute('''SELECT State, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM agg_trans GROUP BY State 
                                         ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total Amount', 'Total Count']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - :violet[Lakshadweep] leads the list in being the top state with the lowest transaction amount and count amounting to
                                            only a little above **1 Billion worth of transactions** and about **419.7 thousand number of transactions** throughout the years.
                                            - The States of :violet[Mizoram] and :violet[Andaman & Nicobar Islands] rank as the 2nd and 3rd on list having the least
                                            amount of transactions.
                                            - All the states in this list (mostly around the North Eastern part of the country) are :violet[sparsely populated] ones with rough terrains 
                                            and areas with seasonal fluctuations; naturally yielding to lesser number of and amount of transactions.
                                            ''')
        
        if qns == "2. Top 10 Districts: Highest and Lowest Transaction Amounts (with counts)":
                st.title(":violet[Top 10 Districts : Highest & Lowest Transactions]")
                st.write('')
                col1,col2 = st.columns([1.5,1.8],gap="large")
        
                with col1:
                        st.subheader(":violet[Highest Transaction Amount and Counts - Districts]")
                        mycursor.execute('''SELECT District, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                sum(Transaction_count) AS 'Total Count' FROM map_trans GROUP BY District 
                                ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total Amount', 'Total Count'])
                        fig = px.bar(df, x= 'Total Amount', y = 'District', orientation='h', 
                                        color = 'Total Amount', color_continuous_scale=px.colors.sequential.Greens,
                                        hover_data=['Total Count'], labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
        
                with col2:
                        st.subheader(":violet[Lowest Transaction Amount and Counts - Districts]")
                        st.write(' ')
                        mycursor.execute('''SELECT District, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                        sum(Transaction_count) AS 'Total Count' FROM map_trans GROUP BY District 
                                        ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total Amount', 'Total Count'])
                        fig = px.bar(df, x= 'Total Amount', y = 'District', orientation='h', 
                                color = 'Total Amount',
                                color_continuous_scale=px.colors.sequential.Burg,
                                hover_data=['Total Count'],
                                labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
        
                c1,c2 = st.columns([1.5,1.5], gap="small")
                with c1:
                        st.subheader(":violet[Highest Transaction Districts - Table]")
                        mycursor.execute('''SELECT District, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                        sum(Transaction_count) AS 'Total Count' FROM map_trans GROUP BY District 
                                        ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total Amount', 'Total Count']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                - :violet[Bengaluru Urban District] leads the list in being the top District with highest transaction amount amounting to
                                **14.7 Trillion worth of transactions**, followed closely by :violet[Hyderabad District] on the 2nd with 
                                roughly **10.2 Trillion** and :violet[Pune District] with **7.4 Trillion** worth of transactions. 
                                - The top 3 District are again, :violet[_technologically advanced_] areas of the country seeing a lot of digital transactions on a day-to-day basis,
                                leading to their prominence in the app.
                                - :violet[_Bengaluru Urban District_] has without doubt seen itself on the top of the transaction counts list with 12.3 billion transactions so far.
                                - The other Districts following close behind are from the states of :violet[_Rajasthan, Telangana, Andhra Pradesh_] and :violet[_Bihar_] forming the majority of the top places
                                owing to their technological advancements and population.
                                ''')
                with c2:
                        st.subheader(":violet[Lowest Transaction Districts - Table]")
                        mycursor.execute('''SELECT District, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                sum(Transaction_count) AS 'Total Count' FROM map_trans GROUP BY District 
                                ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total Amount', 'Total Count']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df) 
                        st.write(' ')
                        i2 = st.button("Insights for L10")
                        if i2:
                                st.markdown('''
                                - :violet[Pherzawl District] belonging to the State of Manipur leads the list in being the top District with the lowest transaction amount and count amounting to
                                only a little above **144 Million worth of transactions** and about **53.3 thousand number of transactions** throughout the years.
                                - The proceeding districts of :violet[Dibang Valley and Pakke Kessang] of Arunachal Pradesh are less populated regions leading to fewer transactions.
                                - Once again, most of the districts here come from the north eastern regions around mountain ranges where :violet[_internet infrastructure is not highly suitable_] for digital transactions.
                                - Socioeconomic factors and cultural :violet[_preferences for cash transactions_] also contribute to 
                                lower digital payment adoption in these regions.
                                ''')
        
        if qns == "3. Top 10 Pincodes: Highest and Lowest Transaction Amounts (with counts)":
                st.title(":violet[Top 10 Pincodes : Highest & Lowest Transactions]")
                st.write('')
                col1,col2 = st.columns([1.5,1.5],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Transaction Amount and Counts - Pincodes]")
                        mycursor.execute('''SELECT Pincode, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM top_trans GROUP BY Pincode 
                                         ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total Amount', 'Total Count'])
                        fig = px.pie(df, names='Pincode', values='Total Amount',
                                                color_discrete_sequence=px.colors.sequential.PuBuGn_r,
                                                hover_data=['Total Count'],
                                                labels={'Transactions_Count':'Total Count'},
                                                hole = 0.5)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)

                
                with col2:
                        st.subheader(":violet[Lowest Transaction Amount and Counts - Pincodes]")
                        mycursor.execute('''SELECT Pincode, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM top_trans GROUP BY Pincode 
                                         ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total Amount', 'Total Count'])
                        fig = px.pie(df, names='Pincode', values='Total Amount',
                                                color_discrete_sequence=px.colors.sequential.Burgyl,
                                                hover_data=['Total Count'],
                                                labels={'Transactions_Count':'Total Count'},
                                                hole = 0.5)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="small")
                with c1:
                        st.subheader(":violet[Highest Transaction Pincodes - Table]")
                        mycursor.execute('''SELECT Pincode, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM top_trans GROUP BY Pincode 
                                         ORDER BY round(sum(Transaction_amount),2) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total Amount', 'Total Count']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[Hyderabad] pincodes lead the list in the 1st two places with the highest transaction amount amounting to
                                            roughly **3 Trillion worth of transactions** and **2.7 Trillion** respectively, followed closely by :violet[Bengaluru] pincode
                                            on the 3rd with roughly **2.1 Trillion**, followed by :violet[Delhi and Pune] pincodes with **1.8 Trillion** worth of transactions each. 
                                            - These pincodes are some of the most developed areas of the country with flourishing IT presence,
                                            leading to higher digital activity when it comes to transactions.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Transaction Pincodes - Table]")
                       mycursor.execute('''SELECT Pincode, round(sum(Transaction_amount),2) AS 'Total Amount', 
                                         sum(Transaction_count) AS 'Total Count' FROM top_trans GROUP BY Pincode 
                                         ORDER BY round(sum(Transaction_amount),2) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total Amount', 'Total Count']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - The pincodes belonging to the region of :violet[Aizawl ,Mizoram] has the 2 least amount
                                            of transactions which is about **866 thousand** and **1.4 Million** users respectively, followed by
                                            a district in Meghalaya accounting to roughly **1.5 Million** worth of transactions taking the 3rd place.
                                            - The others include pincodes from Jammu Kashmir, Tripura, Andaman & Nicobar, etc. which are not densely populated
                                            regions leading to less transactions happening digitally.
                                            ''')
                                
        if qns == "4. Top State: Highest and Lowest performing State annually based on Transaction Amount ":
                st.title(":violet[Top State : Highest & Lowest Transactions annually]")
                st.write('')
                col1,col2 = st.columns([1.6,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Transaction Amount annually - State]")
                        mycursor.execute('''SELECT Year, State, TotalAmount FROM (
                                         SELECT Year, State, TotalAmount, RANK() OVER (PARTITION BY Year ORDER BY TotalAmount DESC) AS Rk 
                                         FROM (
                                         SELECT Year, State, ROUND(SUM(Transaction_amount),2) AS TotalAmount 
                                         FROM agg_trans GROUP BY Year, State) AS yearly_totals
                                         ) AS Ranked_totals where Rk=1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'State','Total Amount'])
                        fig = px.bar(df, y= 'Year', x = 'Total Amount', orientation='h', 
                                color = 'State',
                                # color_continuous_scale=px.colors.sequential.Burg,
                                hover_data=['State'],
                                labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)

                
                with col2:
                        st.subheader(":violet[Lowest Transaction Amount annually - State]")
                        mycursor.execute('''SELECT Year, State, TotalAmount FROM (
                                         SELECT Year, State, TotalAmount, RANK() OVER (PARTITION BY Year ORDER BY TotalAmount) AS Rk 
                                         FROM (
                                         SELECT Year, State, ROUND(SUM(Transaction_amount),2) AS TotalAmount 
                                         FROM agg_trans GROUP BY Year, State) AS yearly_totals
                                         ) AS Ranked_totals where Rk=1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'State','Total Amount'])
                        fig = px.bar(df, y = 'Year', x = 'Total Amount', orientation='h', 
                                color = 'State',
                                # color_continuous_scale=px.colors.sequential.Burg,
                                hover_data=['State'],
                                labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="small")
                with c1:
                        st.subheader(":violet[Highest Transaction Amount annually - Table]")
                        mycursor.execute('''SELECT Year, State, TotalAmount FROM (
                                         SELECT Year, State, TotalAmount, RANK() OVER (PARTITION BY Year ORDER BY TotalAmount DESC) AS Rk 
                                         FROM (
                                         SELECT Year, State, ROUND(SUM(Transaction_amount),2) AS TotalAmount 
                                         FROM agg_trans GROUP BY Year, State) AS yearly_totals
                                         ) AS Ranked_totals where Rk=1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'State','Total Amount']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[Maharashtra] has topped the highest transaction amount list in 2018 with its 189 Billion
                                            worth of transactions, followed by :violet[Karnataka] in 2019 with a significant increase to **791 Billion**
                                            worth of amount.
                                            - :violet[Telangana] has bagged the next highest amount in the next 3 years until 2022 with gradual increase,
                                            owing to its technological and IT growth, now taken over by :violet[Karnataka] in the last 2 years proving their presence
                                            in the digital transaction world due to many IT professionals seeking jobs and relocating there.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Transaction Amount annually - Table]")
                       mycursor.execute('''SELECT Year, State, TotalAmount FROM (
                                         SELECT Year, State, TotalAmount, RANK() OVER (PARTITION BY Year ORDER BY TotalAmount) AS Rk 
                                         FROM (
                                         SELECT Year, State, ROUND(SUM(Transaction_amount),2) AS TotalAmount 
                                         FROM agg_trans GROUP BY Year, State) AS yearly_totals
                                         ) AS Ranked_totals where Rk=1 ORDER BY Year;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'State','Total Amount']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - :violet[Lakshadweep] has remained to be the only State in the list of least transactions
                                            seen in all these years consequently.
                                            - Reasons include sparse population and seasonal fluctuations during tourist visits, with very
                                            minimum usage of digital modes of transactions.
                                            ''')
        
        if qns == "5. Top Types: Highest Transaction Types by Transactions":
                st.title(":violet[Top Types : Highest Transaction Types by Transactions]")
                st.write('')
                col1,col2 = st.columns([1.6,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Top Types by Highest Transaction Amount]")
                        mycursor.execute('''select Transaction_type as Type, sum(Transaction_count) as 'Total Count', 
                                         round(sum(Transaction_amount),2) as 'Total Amount' from agg_trans 
                                         group by Transaction_type order by sum(Transaction_amount) desc;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Type', 'Total Count','Total Amount'])
                        fig = px.bar(df, x= 'Type', y = 'Total Amount', orientation='v', 
                                color = 'Type',
                                # color_continuous_scale=px.colors.sequential.Burg,
                                hover_data=['Total Amount'],
                                labels={'Transaction_amount':'Total Amount'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)

                
                with col2:
                        st.subheader(":violet[Top Types by Highest Transaction Count]")
                        mycursor.execute('''select Transaction_type as Type, sum(Transaction_count) as 'Total Count', 
                                         round(sum(Transaction_amount),2) as 'Total Amount' from agg_trans 
                                         group by Transaction_type order by sum(Transaction_count) desc;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Type', 'Total Count','Total Amount'])
                        fig = px.bar(df, x = 'Type', y = 'Total Count', orientation='v', 
                                color = 'Type',
                                # color_continuous_scale=px.colors.sequential.Burg,
                                hover_data=['Total Count'],
                                labels={'Transaction_count':'Total Count'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="large")
                with c1:
                        st.subheader(":violet[Top Types by Highest Transaction Amount - Table]")
                        mycursor.execute('''select Transaction_type as Type, sum(Transaction_count) as 'Total Count', 
                                         round(sum(Transaction_amount),2) as 'Total Amount' from agg_trans 
                                         group by Transaction_type order by sum(Transaction_amount) desc;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Type', 'Total Count','Total Amount']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                        - The type of transaction leading to maximum amount is the :violet[Peer-to-peer payment] which contributed
                                        to about **192 Trillion** in total throughout the years, followed by :violet[Merchant payments] attributing
                                        to **43.3 Trillion** in total followed by :violet[Recharge and Bill payments] amounting to **9.6 Trillion**
                                        - The drastic difference between the first 2 types shows how digital transactions have been commonly and significantly
                                            large amounts are transacted between peers or known contacts.
                                        ''')
                with c2:
                        st.subheader(":violet[Top Types by Highest Transaction Count - Table]")
                        mycursor.execute('''select Transaction_type as Type, sum(Transaction_count) as 'Total Count', 
                                         round(sum(Transaction_amount),2) as 'Total Amount' from agg_trans 
                                         group by Transaction_type order by sum(Transaction_count) desc;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Type', 'Total Count','Total Amount']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df) 
                        st.write(' ')
                        i2 = st.button("Insights for L10")
                        if i2:
                                st.markdown('''
                                        - :violet[Merchant payments] seem to lead the table with **82.3 Billion** number of transactions over the years
                                            followed by :violet[Peer-to-peer payments] of about **59 Billion** transaction counts and taken over by
                                            :violet[Recharge and Bill payments] with **15 Billion** transactions.
                                        - Although the merchant payments have the highest count of transactions, the peer-to-peer type far exceeds the
                                            transaction amount meaning considerable larger sum of money is transacted between contacts using the app when compared to
                                            the merchant payments which maybe many day-to-day small amounts.
                                        ''')
                                
        if qns == "6. Top 10 States: Highest and Lowest User counts":
                st.title(":violet[Top 10 States : Highest & Lowest Registered Users]")
                st.write('')
                col1,col2 = st.columns([1.5,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Registered Users - States]")
                        mycursor.execute('''SELECT State, sum(User_count) AS 'Users'
                                         FROM agg_user GROUP BY State ORDER BY sum(User_count) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Users'])
                        df['State'].replace({'Dadra and Nagar Haveli and Daman and Diu': 'Dadra'}) 
                        fig = px.pie(df, names='State', values='Users',
                                                color_discrete_sequence=px.colors.sequential.PuBuGn_r,
                                                labels={'User_count':'Users'},
                                                hole = 0.5)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest Registered Users- States]")
                        mycursor.execute('''SELECT State, sum(User_count) AS 'Users' 
                                         FROM agg_user GROUP BY State ORDER BY sum(User_count) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Users'])
                        df['State'] = df['State'].replace({'Dadra and Nagar Haveli and Daman and Diu': 'Dadra'}) 
                        fig = px.pie(df, names='State', values='Users',
                                                color_discrete_sequence=px.colors.sequential.Burgyl,
                                                labels={'User_count':'Users'},
                                                hole = 0.5)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="small")
                with c1:
                        st.subheader(":violet[Highest Registered Users - Table]")
                        mycursor.execute('''SELECT State, sum(User_count) AS 'Users'
                                         FROM agg_user GROUP BY State ORDER BY sum(User_count) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Users']).reset_index(drop=True)
                        df['State'].replace({'Dadra and Nagar Haveli and Daman and Diu': 'Dadra'})
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[Maharashtra] leads the list in being the top state with highest users with about
                                            **452 Million**, followed closely by :violet[Uttar Pradesh] on the 2nd with 
                                            roughly **356 Million** and :violet[Karnataka] with **291 Million** users. 
                                            - The list is followed by :violet[Andhra Pradesh, Rajasthan, Telangana, West Bengal] with about
                                            **200 Million** users each.
                                            - All these states are densely populated ones, with many people registering on
                                            a regular basis and making use of  digital transactions.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Registered Users - Table]")
                       mycursor.execute('''SELECT State, sum(User_count) AS 'Users' 
                                         FROM agg_user GROUP BY State ORDER BY sum(User_count) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Users']).reset_index(drop=True)
                       df['State'] = df['State'].replace({'Dadra and Nagar Haveli and Daman and Diu': 'Dadra'})
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - :violet[Lakshadweep] leads the list in being the top state with the lowest user count amounting to only **51 Thousand**
                                            users, followed by :violet[Andaman & Nicobar Islands] with **623 Thousand** users and :violet[Ladakh] with **840 thousand** users.
                                            - The other states primarily consist of :violet[_north eastern states_] namely Mizoram, Sikkim, Meghalaya, etc.
                                            - Their sparse population and simple way of living does not give rise to adaptation to fully digital finances.
                                            ''')
                                
        if qns == "7. Top 10 Mobile Brands: Highest and Lowest User counts":
                st.title(":violet[Top 10 Brands : Highest and Lowest Registered User Counts]")
                st.write('')
                col1,col2 = st.columns([1.5,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Registered Users - Brands]")
                        mycursor.execute('''SELECT Brands, sum(User_count) AS 'Users' FROM agg_user 
                                         GROUP BY Brands ORDER BY sum(User_count) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'Users'])
                        fig = px.pie(df, names='Brands', values='Users',
                                                color_discrete_sequence=px.colors.sequential.Tealgrn,
                                                labels={'User_count':'Users'},
                                                hole = 0.4)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest Registered Users - Brands]")
                        mycursor.execute('''SELECT Brands, sum(User_count) AS 'Users' FROM agg_user 
                                         GROUP BY Brands ORDER BY sum(User_count) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'Users'])
                        fig = px.pie(df, names='Brands', values='Users',
                                                color_discrete_sequence=px.colors.sequential.matter,
                                                labels={'User_count':'Users'},
                                                hole = 0.4)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="large")
                with c1:
                        st.subheader(":violet[Highest Registered Users by Brand - Table]")
                        mycursor.execute('''SELECT Brands, sum(User_count) AS 'Users' FROM agg_user 
                                         GROUP BY Brands ORDER BY sum(User_count) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'Users']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - Xiaomi, Samsung, Vivo, and Oppo dominate transactions due to their wide range of products and strong brand recognition.
                                            - Realme, Motorola, and OnePlus gain market share with competitive pricing and innovative features.
                                            - Apple and Huawei maintain transaction volumes through premium branding and advanced technology.
                                            - All these above brands have loyal customer base, service and cost-efficient models that people love, hence
                                            having higher users.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Registered Users by Brand - Table]")
                       mycursor.execute('''SELECT Brands, sum(User_count) AS 'Users' FROM agg_user 
                                         GROUP BY Brands ORDER BY sum(User_count) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'Users']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - In this list of lowest users brands, we have COOLPAD, Lyf, HMD Global on the top 3 which are seemingly unheard of.
                                            - The next few of Lava, Gionee, Asus, Infinix have a range of 1 Million to 5 Million users which is decent, considering
                                            low product branding.
                                            - Micromax, Tecno, Lenovo are budget friendly brands yet having essential features that are a choice for poeple wanting
                                            affordable phones and have a larger user base ranging between 11 to 42 Million users.
                                            ''')

        if qns == "8. Top 10 Districts: Highest and Lowest App Opens":
                st.title(":violet[Top 10 Districts : Highest and Lowest App Opens]")
                st.write('')
                col1,col2 = st.columns([1.6,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest App Opens - Districts]")
                        mycursor.execute('''select District, sum(Registered_users) as 'Users', 
                                         sum(App_Opens) as 'Opens' FROM map_user GROUP BY District
                                         ORDER BY sum(App_Opens) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Users', 'Opens'])
                        fig = px.bar(df, x = 'District', y = 'Opens', orientation='v', 
                                color = 'Users',
                                color_discrete_sequence=px.colors.sequential.Tealgrn,
                                hover_data=['Opens'],
                                labels={'Registered_users':'Users'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest App Opens - Districts]")
                        mycursor.execute('''select District, sum(Registered_users) as 'Users', 
                                         sum(App_Opens) as 'Opens' FROM map_user GROUP BY District
                                         ORDER BY sum(App_Opens) limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Users', 'Opens'])
                        fig = px.bar(df, x = 'District', y = 'Opens', orientation='v', 
                                color = 'Users',
                                color_discrete_sequence=px.colors.sequential.Burgyl,
                                hover_data=['Opens'],
                                labels={'Registered_users':'Users'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="large")
                with c1:
                        st.subheader(":violet[Highest App Opens by Districts - Table]")
                        mycursor.execute('''select District, sum(Registered_users) as 'Users', 
                                         sum(App_Opens) as 'Opens' FROM map_user GROUP BY District
                                         ORDER BY sum(App_Opens) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Users', 'Opens']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[Vijayapura District] leads the list in being the top district with highest User counts and App opens
                                            with about **7 Billion App Open**, followed by :violet[Latur District] on the 2nd with 
                                            roughly **4.7 Billion App Opens** and :violet[Bhilwara District] with roughly ** 4 Billion App Opens** 
                                            - :violet[_Vijayapura District_] in Karnataka is known to be famous for art and historical monuments, making it a tourist destination while
                                            :violet[_Latur District_] of Maharashtra, being the :violet[highest sugar producing district of India] takes over in the trade making them
                                            digitally active districts seeing many transactions on a daily basis, owing to high number of app opens.
                                            - :violet[_Bhilwara District_] of Rajasthan, called the **textile city** has also seen large number of app opens owing to their trade.
                                            - All the other districts have seen a significant number of app opens of more than 2 billion.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest App Opens by Districts - Table]")
                       mycursor.execute('''select District, sum(Registered_users) as 'Users', 
                                         sum(App_Opens) as 'Opens' FROM map_user GROUP BY District
                                         ORDER BY sum(App_Opens) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Users', 'Opens']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - :violet[Pherzawl District] of Manipur, similar to having low transactions also sees itself with the lowest app opens, followed by 2 other
                                            districts of :violet[Chandel] and :violet[Kamjong] all from Manipur.
                                            - This is followed by Lower Siang and Anjaw districts of Arunachal Pradesh, similar to having low transactions.
                                            - All the districts in this list (mostly around the North Eastern part of the country) are :violet[sparsely populated] ones with rough terrains 
                                            and areas with seasonal fluctuations; naturally yielding to very less digital engagement.
                                            ''')
                                
        if qns == "9. Top 10 Pincodes: Highest and Lowest Registered Users":
                st.title(":violet[Top 10 PIncodes : Highest and Lowest Registered Users]")
                st.write('')
                col1,col2 = st.columns([1.6,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest Registered Users - Pincodes]")
                        mycursor.execute('''select Pincode, sum(Registered_users) as 'Users' 
                                         FROM top_user GROUP BY Pincode
                                         ORDER BY sum(Registered_users) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Users'])
                        fig=px.pie(df,names='Pincode',values='Users',
                                                color="Pincode",
                                                color_discrete_sequence=px.colors.sequential.Teal,
                                                labels={'User_count':'Users'},
                                                hole = 0.4)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest Registered Users - Pincodes]")
                        mycursor.execute('''select Pincode, sum(Registered_users) as 'Users' 
                                         FROM top_user GROUP BY Pincode
                                         ORDER BY sum(Registered_users) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Users'])
                        fig=px.pie(df,names='Pincode',values='Users',
                                                color="Pincode",
                                                color_discrete_sequence=px.colors.sequential.matter,
                                                labels={'User_count':'Users'},
                                                hole = 0.4)
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="large")
                with c1:
                        st.subheader(":violet[Highest Registered Users by Pincodes - Table]")
                        mycursor.execute('''select Pincode, sum(Registered_users) as 'Users' 
                                         FROM top_user GROUP BY Pincode
                                         ORDER BY sum(Registered_users) DESC limit 10;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Users']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - The top 3 pincodes belonging to :violet[Noida, West Delhi] and :violet[Bangalore] lead the list 
                                            having the highest users owing to the technological advancements and IT in the areas, leading to more people
                                            being digitally dependent on transactions. 
                                            - Some of the other pins are from Maharashtra, Telangana, Haryana and Gujarat showing their prominence in the app,
                                            owing to adopting modernised way of living.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest Registered Users by Pincodes - Table]")
                       mycursor.execute('''select Pincode, sum(Registered_users) as 'Users' 
                                         FROM top_user GROUP BY Pincode
                                         ORDER BY sum(Registered_users) limit 10;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Users']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - The top 3 pincodes belonging to :violet[Kiltan district, Bitrarakhong district] of west Imphal 
                                            and :violet[Laban], East Khasi Hills district lead the list of having least number of app user registration,
                                            owing to the regions' terrains not highly supporting internet facilities.
                                            - Some of the other pins are from coastal or mountanous areas like Goa, the Andaman's, Jammu & Kashmir, etc.                                      owing to adopting modernised way of living.
                                            ''')
                                
        if qns == "10. Top District: Highest and Lowest performing District annually by User Counts":
                st.title(":violet[Highest and Lowest performing District annually by User Counts]")
                st.write('')
                col1,col2 = st.columns([1.6,1.6],gap="large")
                
                with col1:
                        st.subheader(":violet[Highest performing District annually by User Counts]")
                        mycursor.execute('''SELECT Year, District, TotalUsers FROM 
                                         (SELECT Year, District, TotalUsers, 
                                         RANK() OVER (PARTITION BY Year ORDER BY TotalUsers DESC) AS Rk
                                         FROM 
                                         (SELECT Year, District, SUM(Registered_users) AS TotalUsers
                                         FROM map_user GROUP BY Year, District) AS yearly_district_totals
                                         ) AS ranked_district_totals WHERE Rk = 1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'District','TotalUsers'])
                        fig = px.bar(df, y = 'Year', x = 'TotalUsers', orientation='h', 
                                color = 'District',
                                color_discrete_sequence=px.colors.sequential.Tealgrn,
                                hover_data=['TotalUsers'],
                                labels={'Registered_users':'TotalUsers'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                with col2:
                        st.subheader(":violet[Lowest performing District annually by User Counts]")
                        mycursor.execute('''SELECT Year, District, TotalUsers FROM 
                                         (SELECT Year, District, TotalUsers, 
                                         RANK() OVER (PARTITION BY Year ORDER BY TotalUsers) AS Rk
                                         FROM 
                                         (SELECT Year, District, SUM(Registered_users) AS TotalUsers
                                         FROM map_user GROUP BY Year, District) AS yearly_district_totals
                                         ) AS ranked_district_totals WHERE Rk = 1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'District','TotalUsers'])
                        fig = px.bar(df, y = 'Year', x = 'TotalUsers', orientation='h', 
                                color = 'District',
                                color_discrete_sequence=px.colors.sequential.Burgyl,
                                hover_data=['TotalUsers'],
                                labels={'Registered_users':'TotalUsers'})
                        fig.update_layout(showlegend=True)
                        st.plotly_chart(fig,use_container_width=True)
                
                c1,c2 = st.columns([1.5,1.5], gap="large")
                with c1:
                        st.subheader(":violet[Highest performing District annually by User Counts - Table]")
                        mycursor.execute('''SELECT Year, District, TotalUsers FROM 
                                         (SELECT Year, District, TotalUsers, 
                                         RANK() OVER (PARTITION BY Year ORDER BY TotalUsers DESC) AS Rk
                                         FROM 
                                         (SELECT Year, District, SUM(Registered_users) AS TotalUsers
                                         FROM map_user GROUP BY Year, District) AS yearly_district_totals
                                         ) AS ranked_district_totals WHERE Rk = 1 ORDER BY Year;''')
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'District','TotalUsers']).reset_index(drop=True)
                        df.index += 1
                        st.dataframe(df)
                        st.write(' ')
                        i1 = st.button("Insights for H10")
                        if i1:
                                st.markdown('''
                                            - :violet[**Vijayapura District**] of Karnataka takes all the places of being the
                                            highest performing district in the country annually in terms of User counts.
                                            - Being culturally and architecturally rich, it has garnered tourists increasing business in the place,
                                            contributing to its digital presence.
                                            ''')
                with c2:
                       st.subheader(":violet[Lowest performing District annually by User Counts - Table]")
                       mycursor.execute('''SELECT Year, District, TotalUsers FROM 
                                         (SELECT Year, District, TotalUsers, 
                                         RANK() OVER (PARTITION BY Year ORDER BY TotalUsers) AS Rk
                                         FROM 
                                         (SELECT Year, District, SUM(Registered_users) AS TotalUsers
                                         FROM map_user GROUP BY Year, District) AS yearly_district_totals
                                         ) AS ranked_district_totals WHERE Rk = 1 ORDER BY Year;''')
                       df = pd.DataFrame(mycursor.fetchall(), columns=['Year', 'District','TotalUsers']).reset_index(drop=True)
                       df.index += 1
                       st.dataframe(df) 
                       st.write(' ')
                       i2 = st.button("Insights for L10")
                       if i2:
                                st.markdown('''
                                            - :violet[Kangpokpi District] of Manipur takes the first and second place being the least performing district
                                            in terms of user counts, followed by :violet[Srinaar District] for the next 3 years between 2020 and 2022, and
                                            :violet[Lower Siang District] of Arunachal Pradesh taking on in 2023 and 2024.
                                            - Being sparsely populated and also less digitally engaged, these districts seem to have very less digital users.
                                            ''')
                                
