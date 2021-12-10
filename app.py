import streamlit as st
import pandas as pd
import analysisfunction as af
import plotly.express as px

df = pd.read_csv("Finally_Fully_Scraped_Pokemon_Data.csv")
df = af.preprocess(df)

st.set_page_config(layout='wide')
st.sidebar.title("Pokemon Analysis")


user_menu = st.sidebar.radio(
        'Selection Option',
        ('Overall Analysis','Type wise Analysis','Pokemon wise Analysis')
    )


if user_menu == 'Overall Analysis':

    st.header('Statistical Analysis')

    total_Pokemon = len(df['pokemon'].unique())
    lst_abilities = df['Ability_1'].to_list() + df['Ability_2'].to_list()
    lst_abilities = list(set(lst_abilities))
    lst_abilities.remove('None')
    tota_ab = len(lst_abilities)
    lst_types = df['Type_1'].to_list() + df['Type_2'].to_list()
    lst_types = list(set(lst_types))
    lst_types.remove('None')
    tota_t = len(lst_types)
    total_cat = len(df['Category'].unique())
    total_t1 = df['pokemon'][df['Type_2'] == 'None'].count()
    total_t2 = df['pokemon'][df['Type_2'] != 'None'].count()
    total_ab1 = df['pokemon'][df['Ability_2'] == 'None'].count()
    total_ab2 = df['pokemon'][df['Ability_2'] != 'None'].count()

    

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric(label = "Total Pokemon",value = total_Pokemon)

    with col2:
        st.metric(label = "Total Abilities of Pokemon",value = tota_ab)
    
    with col3:
        st.metric(label = "Total Types of Pokemon",value = tota_t)

    with col4:
        st.metric(label = "Total Categories of Pokemon",value = total_cat)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric(label = "Pokemons with only one Type",value = int(total_t1))

    with col2:
        st.metric(label = "Pokemons with two Types",value = int(total_t2))
    
    with col3:
        st.metric(label = "Total Pokemon",value = int(total_ab1))

    with col4:
        st.metric(label = "Pokemons with two Abilities",value = int(total_ab2))

    st.markdown("""---""")
    st.header("Evolution types Count")
    fig = af.Ecoluation_count_plot(df)
    st.plotly_chart(fig)

    st.markdown("""---""")
    st.header("Pokemon Types Count")
    fig = af.Types_count_plot(df)
    st.plotly_chart(fig)

    st.header("Frequency Distributions")
    hist_lables = df.select_dtypes(include='number').columns.to_list()

    hist_input = st.selectbox('Select Column',hist_lables)

    fig = af.hist(df,hist_input)
    st.plotly_chart(fig)


def type_input_plots(dataset):
    st.header("Best Pokemon in each skill")
    col1,col2,col3 = st.columns(3)
    with col1:
        fig = af.Top_five(dataset,'Total')
        st.plotly_chart(fig)
    with col2:
        fig = af.Top_five(dataset,'Speed')
        st.plotly_chart(fig)
    with col3:
        fig = af.Top_five(dataset,'HP')
        st.plotly_chart(fig)

    col1.col2 = st.columns(2)
    with col1:
        fig = af.Top_five(dataset,'Attack')
        st.plotly_chart(fig)
    with col2:
        fig = af.Top_five(dataset,'Defense')
        st.plotly_chart(fig)

    col1.col2 = st.columns(2)
    with col1:
        fig = af.Top_five(dataset,'Sp.Atk')
        st.plotly_chart(fig)
    with col2:
        fig = af.Top_five(dataset,'Sp.Def')
        st.plotly_chart(fig)


if user_menu == 'Type wise Analysis':

    st.sidebar.subheader("Pure Type or Hybrid Type")
    st.sidebar.write("Pure Type : Pokemon having only one Type","\n","Hybrid Type : Pokemon having two Types")


    type_input = st.sidebar.radio(
        'Select',
        ('All Types', 'Pure Type', 'Hybrid Type')
    )

    if type_input == 'All Types':
        df_all_T = af.All_Types(df)
        type_input_plots(df_all_T)
        st.markdown("""---""")
        st.header("Detail Dataframe")
        st.dataframe(df_all_T[['pokemon', 'Type_1', 'Type_2', 'Ability_1', 'Ability_2', 'Hidden_Ability']])

    if type_input == 'Pure Type':
        type1_lst = af.type1list(df)
        tp_input1 = st.sidebar.selectbox('Select Type',type1_lst)
        Pure_Type_df = af.Pure_Type(df,tp_input1)
        type_input_plots(Pure_Type_df)
        st.markdown("""---""")
        st.header("Detail Dataframe")
        st.dataframe(Pure_Type_df[['pokemon', 'Type_1', 'Type_2', 'Ability_1', 'Ability_2', 'Hidden_Ability']])

    if type_input == 'Hybrid Type':
        type1_lst = af.type1list(df)
        tp_input1 = st.sidebar.selectbox('Select Type1',type1_lst)
        type2_lst = af.type2list(df,tp_input1)
        tp_input2 = st.sidebar.selectbox('Select Type2',type2_lst)
        Hybrid_Type_df = af.Hybrid_Type(df,tp_input1,tp_input2) 
        type_input_plots(Hybrid_Type_df)
        st.markdown("""---""")
        st.header("Detail Dataframe")
        st.dataframe(Hybrid_Type_df[['pokemon', 'Type_1', 'Type_2', 'Ability_1', 'Ability_2', 'Hidden_Ability']])

if user_menu == 'Pokemon wise Analysis':

    st.header("Pokemon Details")
    pokemon_list = af.Pokemon_list(df)

    pokemon_input = st.selectbox('Select Pokemon',pokemon_list)

    data_poke = af.Poke_data(df,pokemon_input)

    Pokemon = list(data_poke['pokemon'])[0]
    poke_image = f'https://img.pokemondb.net/artwork/{str(Pokemon).lower()}.jpg'
    Total = list(data_poke['Total'])[0]
    Category = list(data_poke['Category'])[0]
    Hidden_Ability = list(data_poke['Hidden_Ability'])[0]
    Ability_1 = list(data_poke['Ability_1'])[0]
    Ability_2 = list(data_poke['Ability_2'])[0]
    Type_1 = list(data_poke['Type_1'])[0]
    Type_2 = list(data_poke['Type_2'])[0]
    Height = list(data_poke['Height'])[0]
    Weight = list(data_poke['Weight'])[0]
    HP = list(data_poke['HP'])[0]
    Speed = list(data_poke['Speed'])[0]   
    Attack = list(data_poke['Attack'])[0]
    Defense = list(data_poke['Defense'])[0]
    Sp_Atk = list(data_poke['Sp.Atk'])[0]
    Sp_Def = list(data_poke['Sp.Def'])[0]

    st.sidebar.image(poke_image,width=200)

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Pokemon',value=Pokemon)
    with col2:
        st.metric('Total',value=Total)
    with col3:
        st.metric('Category',value=Category)
    with col4:
        st.metric('Hidden_Ability',value=Hidden_Ability)

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('First Type',value=Type_1)
    with col2:
        st.metric('Second Type',value=Type_2)
    with col3:
        st.metric('First Ability',value=Ability_1)
    with col4:
        st.metric('Second Ability',value=Ability_2)

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Height',value=Height)
    with col2:
        st.metric('Weight',value=Weight)
    with col3:
        st.metric('Speed',value=Speed)
    with col4:
        st.metric('HP',value=HP)

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Attack',value=Attack)
    with col2:
        st.metric('Defense',value=Defense)
    with col3:
        st.metric('Special Attack',value=Sp_Atk)
    with col4:
        st.metric('Special Defense',value=Sp_Def)

    st.markdown("""---""")
    st.subheader("Weakness")
    if list(data_poke['Weaknesses'])[0] == '[]':
        st.write("There is no any weakness of "+Pokemon+" or we don't know yet.")
    else:
        data_weakness = af.show_weakness(df)
        st.table(data_weakness)

    st.markdown("""---""")
    st.subheader("Evolution")
    if list(data_poke['Evolutions'])[0] == 'None':
        st.write("There is no any evolution of "+Pokemon+" or we don't know yet.")
    else:
        data_evo = af.show_evolution(data_poke)
        st.table(data_evo)

    st.markdown("""---""")
    st.subheader("Description")

    desc = af.show_description(data_poke)
    st.subheader(desc)
