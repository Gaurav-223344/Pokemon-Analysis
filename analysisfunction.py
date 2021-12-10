import pandas as pd
import numpy as np
import plotly.express as px

def preprocess(df):
    df.drop(['index'], axis=1, inplace=True)

    # replace all null values will catagory 'None'
    df.fillna('None',inplace=True)

    # converting hight and weight in numeric format
    df['Height'] = df['Height'].apply(lambda X : float(str(X).split("m")[0]))
    df['Weight'] = df['Weight'].apply(lambda X : float(str(X).split("kg")[0]))

    return df

def Ecoluation_count_plot(df):
    data_ET = pd.DataFrame(df['Evolution_type'].value_counts()).sort_values(by='Evolution_type')
    data_ET = data_ET.reset_index()
    data_ET.columns = ['Evolution Type','No. of Pokemon']

    fig = px.bar(data_ET, x='No. of Pokemon', y='Evolution Type', orientation='h')
    fig.update_layout({'plot_bgcolor' : 'rgba(0,0,0,0)', 'paper_bgcolor' : 'rgba(0,0,0,0)'})
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(width=800,height=500)
    return fig

def Types_count_plot(df):
    data_Type1 = pd.DataFrame(df.Type_1.value_counts())
    data_Type2 = pd.DataFrame(df.Type_2.value_counts())
    data_types = data_Type1.join([data_Type2],how='inner')
    data_types['total_types'] = data_types['Type_1'] + data_types['Type_2']
    data_types = data_types.reset_index()
    data_types.columns = ['Type','Pokemon in Type1', 'Pokemon in Type2', 'Total no. of Pokemon']

    fig = px.bar(data_types, x='Type', y='Total no. of Pokemon')
    fig.update_layout({'plot_bgcolor' : 'rgba(0,0,0,0)', 'paper_bgcolor' : 'rgba(0,0,0,0)'})
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(width=800,height=500)
    return fig


def hist(df,column):
    fig = px.histogram(df, x=column)
    fig.update_layout({'plot_bgcolor' : 'rgba(0,0,0,0)', 'paper_bgcolor' : 'rgba(0,0,0,0)'})
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(width=800,height=500)
    return fig


def All_Types(df,type1,type2):
    dataset = df.drop(['Description_X', 'Description_Y', 'Weaknesses', 'Evolutions', 'Evolution_type', 'evolution_list_index'],axis=1)
    if (type1 == 'All') & (type2 == 'All'):
        return dataset
    if (type1 != 'All') & (type2 == 'All'):
        return dataset[dataset['Type_1'] == type1]
    if (type1 == 'All') & (type2 != 'All'):
        return dataset[dataset['Type_2'] == type2]
    if (type1 != 'All') & (type2 != 'All'):
        return dataset[(dataset['Type_1'] == type1) & (dataset['Type_2'] == type2)]
    

def Pure_Type(df,type1):
    dataset = df.copy()
    Pure_Type_df = dataset[dataset['Type_2'] == 'None']
    Pure_Type_df.drop(['Description_X', 'Description_Y', 'Weaknesses', 'Evolutions', 'Evolution_type', 'evolution_list_index'],axis=1,inplace=True)
    if type1 == 'All':
        return Pure_Type_df
    else:
        return Pure_Type_df[Pure_Type_df['Type_1'] == type1]
    

def Hybrid_Type(df,type1,type2):
    dataset = df.copy()
    Hybrid_Type_df = dataset[dataset['Type_2'] != 'None']
    Hybrid_Type_df.drop(['Description_X', 'Description_Y', 'Weaknesses', 'Evolutions', 'Evolution_type', 'evolution_list_index'],axis=1,inplace=True)
    if (type1 == 'All') & (type2 == 'All'):
        return Hybrid_Type_df
    if (type1 != 'All') & (type2 == 'All'):
        return Hybrid_Type_df[Hybrid_Type_df['Type_1'] == type1]
    if (type1 == 'All') & (type2 != 'All'):
        return Hybrid_Type_df[Hybrid_Type_df['Type_2'] == type2]
    if (type1 != 'All') & (type2 != 'All'):
        return Hybrid_Type_df[(Hybrid_Type_df['Type_1'] == type1) & (Hybrid_Type_df['Type_2'] == type2)]
    return Hybrid_Type_df

def Top_five(df,skill):
    temp_data = df.sort_values(by=skill)[['pokemon',skill]].tail(5)
    temp_title = 'Pokemon with best ' + skill
    fig = px.bar(temp_data, x=skill, y='pokemon', orientation='h', title=temp_title)
    fig.update_layout({'plot_bgcolor' : 'rgba(0,0,0,0)', 'paper_bgcolor' : 'rgba(0,0,0,0)'})
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(width=400,height=400)
    return fig

def type1list(df):
    type1lst = list(df['Type_1'].unique())
    type1lst.insert(0,'All')
    return type1lst

def type2list(df,type1):
    temp_data = df[df['Type_1'] == type1]
    lst_type2 = list(temp_data['Type_2'].unique())
    lst_type2.insert(0,'All')
    lst_type2
    return lst_type2

def Pokemon_list(df):
    pokemon_list = df.pokemon.to_list()
    return pokemon_list

def Poke_data(df,pokemon):
    data_poke = df[df['pokemon'] == pokemon ]
    return data_poke

def show_weakness(dataset):
    df = dataset.copy()
    temp_w = list(df['Weaknesses'])[0]
    temp_w = temp_w[1:-1].split(", ")
    weakness_list = [i[1:-1] for i in temp_w]
    data_weak = pd.DataFrame(weakness_list,columns=['weakness'])
    data_weak.index +=1
    return data_weak.transpose()

def show_evolution(dataset):
    df = dataset.copy()
    temp_e = list(df['Evolutions'])[0]
    temp_e = temp_e[1:-1].split(", ")
    evolution_list = [i[1:-1] for i in temp_e]
    data_evo = pd.DataFrame(evolution_list,columns=['Evolutions'])
    data_evo = data_evo.replace(list(df['pokemon'])[0],list(df['pokemon'])[0] + ' *')
    data_evo.index +=1
    return data_evo.transpose()

def show_description(dataset):
    df = dataset.copy()
    if list(df['Description_X'])[0] == list(df['Description_Y'])[0]:
        return list(df['Description_X'])[0]
    else:
        return list(df['Description_X'])[0] +' '+list(df['Description_Y'])[0]

