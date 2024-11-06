import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    h1 {
        color: #B35C37;
        text-align: center;
    }
    h3, h4, h5, h6 {
        color: #B35C37;
    }
    h2, p {
        color: #FFFFFF;
    }
    .stSidebar {
        background-color: #4B3D29;
    }
    .stMain {
        background-color: #FFFFFF; 
    } 
    </style>
    """,
    unsafe_allow_html=True
)

st.title("DashBoard PPGHIS (Alunos e Egressos)")
st.sidebar.header("Menu de Filtragem: ")
st.sidebar.write("Aqui estão alguns filtros e opções.")

# Lista de nomes para filtrar
nomes_para_filtrar = [
    "Adelle Jeanne Santos Sant'Anna",
"Adriano Moura de Oliveira",
"Alan da Silva Rocha",
"Alessandra Nóbrega Monteiro",
"Alexander da Silva Braz",
"Alexandra Sablina do Nascimento Veras",
"Alexia de Santana Rosa",
"Alexia Helena de Araujo Shellard",
"Alípio Pereira do Carmo",
"Alípio Pereira do Carmo",
"Aluan Carlos Gomes",
"Amanda De Carvalho Santos Lima",
"Amanda Dias de Oliveira",
"Amanda Guimarães da Silva",
"Amaro Jose de Souza Neto",
"Ana Beatriz Ferreira Marques",
"Ana Carolina Reginatto Moraes",
"Ana Clara Nunes Tavares",
"Ana Lectícia Felix Angelotti",
"Ana Paula Campos Barra",
"Ana Taisa da Silva Falcão",
"André Alcântara Aguiar",
"André Arioza Vargas",
"André Francisco Berenger de Araujo",
"Andréia Tamanini de Araújo",
"Andressa Melo da Fonseca",
"Angélica Paulillo Ferroni",
"Anne Caroline Santos Nunes",
"Antonio Daniel Correia de Araujo",
"Antonio Paiva Souto Maior",
"Antônio Pedro de Almeida Santos",
"Ariadne Pires Barbosa",
"Ariane Carvalho da Cruz",
"Arnaldo Lucas Pires Junior",
"Augusto Cesar Oliveira Martins",
"Ayra Guedes Garrido",
"Barbara de Almeida Guimarães",
"Bárbara Geromel Campanholo",
"Barbara Mangueira do Nascimento",
"Barbara Maria de Albuquerque Mitchell",
"Beatriz Monteiro Lemos",
"Beatriz Weisheimer de Mendonça",
"Bernardo Moraes Ferreira Reis",
"Bruna Aparecida Gomes Coelho",
"Bruno Azambuja Araujo",
"Bruno Marinho de Matos",
"Bruno Martins de Castro",
"Bruno Rodrigo Couto Lemos",
"Bruno Sousa Silva Godinho",
"Cainã Carneiro Gusmão",
"Caio Marcelo Cabral Vilanova",
"Camila de Oliveira Farias",
"Camila Ferreira Figueiredo",
"Camille Ferreira Leandro",
"Carla Bianca Carneiro Amarante Correia",
"Carla Teodoro Costa",
"Carlos Romário da Silva de Matos",
"Carolina Ferreira de Figueiredo",
"Carolina Mann de Oliveira",
"Carolina Perpétuo Corrêa",
"Caroline Cardoso Planinschek",
"Caroline Rios Costa",
"Celia Daniele Moreira de Souza",
"Clarice Barros Araújo Berkowicz",
"Clemente Gentil Penna",
"Cleudiza Fernandes de Souza",
"Daiani da Silva Barbosa",
"Daniel Dutra Coelho Braga",
"Daniel Teixeira Taveira",
"Daniella Dalla Maestri",
"Danielle Freire da Silva",
"David Durval Jesus Vieira",
"Deborah da Costa Fontenelle",
"Denise da Silva de Oliveira",
"Dhyan Ramayana Ramos Rodrigues",
"Diego de Moraes Campos",
"Diego Knack",
"Dirson Fontes da Silva Sobrinho",
"Dominique Neves Pereira",
"Eduardo Henrique Sabioni Ribeiro",
"Eduardo Martins Jorge",
"Eduardo Santiago Couto",
"Eduardo Tude Falcão",
"Elaine Cristina Ventura Ferreira",
"Elion de Souza Campos",
"Emanuelly Gomes dos Santos Foppa",
"Eraldo de Souza Leão Filho",
"Eric Fagundes de Carvalho",
"Fabio de Mello Baptista",
"Felipe Bernardo da Silva Goebel",
"Felipe da Silva Barbosa",
"Felipe José Souza Fernandes da Silva",
"Fernanda Bana Arouca",
"Fernanda Coelho Mendes",
"Fernanda Coutinho Teixeira",
"Fernanda Gabrielly Terra Moura",
"Fernanda Silva Monteiro Pinto",
"Filipe Duret Athaide",
"Filipe Oliveira da Silva",
"Filipe Pitrosse",
"Gabriel Alencar e Souza",
"Gabriel Almeida Bizzo",
"Gabriel Alves Pereira",
"Gabriel Camejo Sampaio",
"Gabriel Duarte Evangelista da Silva",
"Gabriel Felipe Oliveira de Mello",
"Gabriel Melo Mizrahi",
"Gabriel Pereira de Oliveira",
"Gabriela Fernandes Petrungaro",
"Gabriela Machado do Amaral",
"Geisimara Soares Matos",
"Geison Siqueira Tavares da Cruz",
"Gilberto de Souza Vianna",
"Giovanna Zamith Cesário",
"Giovanna Zamith Cesário",
"Glauber de Oliveira Montes",
"Guilherme Leite Ribeiro",
"Gustavo Junqueira Costa Maia",
"Gustavo Monteiro de Rezende",
"Gustavo Souza de Deus da Silva",
"Hana Mariana da Cruz Ribeiro Costa",
"Helen da Silva Silveira",
"Hendie Tavares Teixeira",
"Henrique Freire de Jesus",
"Henrique Machado Vieira Lopes",
"Iasmin Castro de Souza",
"Inghrid da Costa Masullo Mendes",
"Ingrid Gomes Ferreira",
"Iolanda Chaves Ferreira de Oliveira",
"Isaac Carlos Trevisan da Costa",
"Isabela Frias Masi",
"Isabella dos Santos Daiub",
"Isabella Loureiro Khaled Poppe",
"Isabella Santos Pinheiro",
"Isabella Villarinho Pereyra",
"Isabelle Cristina da Silva Pires",
"Isadora Silva Gomes",
"Ísis Carla Vieira Ferreira Coelho",
"Isis Saraiva Leão Medina",
"Jaime Mitropoulos",
"Janaína Di Lourenço Esteves",
"Jean Pedro Silva de Sousa",
"Jefferson de Albuquerque Mendes",
"Jefferson dos Santos Alves",
"Jerônimo Aguiar Duarte da Cruz",
"Jéssyca Silveira Souza",
"João Fernando Barreto de Brito",
"João Martins Pinheiro Dias Pereira",
"João Paulo Henrique Pinto",
"João Pedro Teixeira Ferreira Thimoteo",
"João Vitor de Oliveira Silva",
"Jônatan Coutinho da Silva de Oliveira",
"Jonathan Cesar Rodrigues",
"Jorge Steimback Barbosa Junior",
"Josemberg Pereira de Araújo",
"Josimar Faria Duarte",
"Julia Amaral Amato Moreira",
"Julia Soares Leite Lanzarini de Carvalho",
"Juliana Assis Nascimento",
"Juliana Batista",
"Juliana Gonçalves de Oliveira Ferreira",
"Juliana Nascimento da Silva",
"Júlio Dória",
"Kamila Gouveia Camargo Cré",
"Keicy Salustiano da Silva",
"Kevin Wetter Pereira Lima",
"Kezia Wandressa da Costa Lima",
"Laís Morgado Marcoje",
"Larissa de Oliveira Farias",
"Lavinia Izidoro Martins",
"Lays Correa da Silva",
"Leandro Arraes Liberali",
"Leandro César Santana Neves",
"Lenilson Nóbrega da Silva de Oliveira",
"Letícia Gomes do Nascimento",
"Letícia Helena de Oliveira",
"Livia Claro Pires",
"Lívia Freitas Pinto Silva Soares",
"Luan Mendes de Medeiros Siqueira",
"Luana Camila Da Silva Rosario",
"Luana Leão Rodrigues",
"Luca Araujo de Oliveira Leite",
"Luca Araujo de Oliveira Leite",
"Lucas Barroso Rego",
"Lucas de Mattos Moura Fernandes",
"Lucas Lixa Victor Neves",
"Lucas Mariel de Carvalho Carnaúba de Menezes",
"Lucas Sampaio Costa Souza",
"Lucas Souza Nascimento",
"Lucas Vinicius Erichsen da Rocha",
"Luciana Campos Batista",
"Luciana Lucia da Silva",
"Luciano Bastos Meron Neves",
"Luis Guilherme Eschenazi Lucena",
"Luis Henrique Souza dos Santos",
"Luís Ricardo Araujo da Costa",
"Luiz Antonio da Silva Teixeira",
"Luiz Felipe Vieira Ferrão",
"Luiza das Neves Gomes",
"Luiza de Paschoal Mohamed",
"Luiza Nascimento de Oliveira da Silva",
"Maicon Mariano",
"Maíra Cristina Tomé Fonseca",
"Márcio de Oliveira Albuquerque",
"Maria Beatriz Gomes Bellens Porto",
"Maria Cristina Portella Ribeiro",
"Maria Eduarda de França Monteiro",
"Maria Vitória de Oliveira Cardoso",
"Mariana Barrozo Gonzalez",
"Mariana Freitas de Andrade",
"Mariana Madruga Bianchini",
"Mariana Nastari Siqueira",
"Mariana Pastana Batista da Silva",
"Marina Salgado Pinto",
"Mário Novaes César Rezende",
"Maristela Santana",
"Matheus Aguiar Duccini Ultra",
"Matheus Almeida Gonçalves Pereira",
"Matheus Brum Domingues Dettmann",
"Matheus Butrucci Gomes",
"Matheus Paranhos Giolo Mezadri",
"Matheus Teixeira Moretti",
"Maya Moldes da Rocha Pereira",
"Mayara de Freitas Portilho Silveira",
"Mayra Mendes Trocado",
"Michelle Alves Pinheiro de Oliveira",
"Michelle Caetano",
"Millena Souza Farias",
"Milleni Freitas Rocha",
"Mirella Soraya Pinheiro Rodrigues de Oliveira",
"Moisés Corrêa Fonseca da Silva",
"Moisés Peixoto Soares",
"Mônica Santos da Silva",
"Murillo Dias Winter",
"Murilo Rosa Garcias",
"Mylena Pereira da Silva",
"Mylena Porto da Gama",
"Naiara Müssnich Rotta Gomes de Assunção",
"Natália de Fátima de Carvalho Lacerda",
"Natalia de Souza Miranda",
"Natasha Augusto Barbosa",
"Natasha Mastrangelo Silva de Moraes",
"Nathália Carvalho da Silveira Assed",
"Nathara Marriel Mariano",
"Nicolas Campelo Pinto de Oliveira",
"Nicolle Sthefane de Oliveira Lima",
"Nicoly Goldschmidt Vitorino",
"Nina Fernandes Cunha Galvao",
"Paola Vargas Arana",
"Patrícia Ramos Geremias",
"Patrick Antunes Menezes",
"Paula Mello dos Santos",
"Paulo Celso Liberato Corrêa",
"Paulo Cesar Machado Farias Junior",
"Paulo Francisco Donadio Baptista",
"Pedro Henrique da Silva Oriola Cardoso",
"Pedro Henrique Ferreira Danese Oliveira",
"Pedro Henrique Garcia Pinto de Araújo",
"Rachel Romano dos Santos",
"Rafael Bezerra Targino",
"Rafael do Nascimento Souza Brasil",
"Rafael Vieira da Cal",
"Rafaela Jacyczen laux",
"Raíra da Cunha Nunes Abi-Ramia",
"Raquel Marques Soares",
"Rebecca Hodesh Muniz de Souza Rozas",
"Renan Perozini Gomes Barrozo",
"Renata da Silva Feliciano",
"Renata Dias Pinto Monteiro",
"Renato Dalcin de Carvalho",
"Ricardo Augusto Pereira",
"Rodrigo Fernandes Antunes Vieira",
"Rodrigo Franco da Costa",
"Rodrigo Maia Monteiro",
"Rodrigo Pereira de Sousa",
"Rodrigo Rocha da Cunha",
"Samuel Barbosa Junior",
"Séfora Semíramis Sutil",
"Suane Felippe Soares",
"Tadeu Alencar de Azevedo Sant Ana Lemos",
"Talita de Jesus Noronha Sanchez",
"Tatiana Rodrigues Gama Russo",
"Tereza Raquel dos Santos Rodrigues",
"Thaís Regina Cardoso Barbosa",
"Thalita Maciel Soares",
"Thayná Fuly Garcia",
"Thays Alves Rodrigues",
"Thiago Figueiredo Martins",
"Thiago Groh de Mello Cesar",
"Thiago Luiz Turibio da Silva",
"Thiago Torres Medeiros da Silva",
"Thiago Vinícius Ferreira",
"Thompson Clímaco Alves",
"Tiago Gomes da Silva",
"Tony Espósito Gonçalves",
"Valéria Dorneles Fernandes",
"Vanderlei Marinho Costa",
"Vanessa de Mendonça Rodrigues dos Santos",
"Vanessa de Souza Vieira da Rocha",
"Vicente Gil da Silva",
"Victor Brandão de Oliveira",
"Victor Lisboa da Fonseca Santos",
"Victor Luiz Alvares Oliveira",
"Victor Moraes Pereira Vianna",
"Victor Serebrenick",
"Victória Ferreira Cunha",
"Vinícius Patrocínio Pereira Costa",
"Vinícius Potrich de Souza Macedo Gonçalves",
"Vinner Stutz de Oliveira",
"Vitor Guilherme Martins",
"Vitória Luyza Cardoso Barbosa",
"Wagner Alcides de Souza",
"Willian Vidal Reis",
"Yasmin Getirana Gonçalves Vicente",
"Yeda Santos de Azambuja Montes"
]

nomes_para_filtrar_egressos = [
    "Adelle Jeanne Santos Sant'Anna",
"Adriano Moura de Oliveira",
"Alan da Silva Rocha",
"Alexander da Silva Braz",
"Alexia Helena de Araujo Shellard",
"Aluan Carlos Gomes",
"Alípio Pereira do Carmo",
"Amanda Dias de Oliveira",
"Ana Carolina Reginatto Moraes",
"Ana Clara Nunes Tavares",
"Ana Taisa da Silva Falcão",
"Andréia Tamanini de Araújo",
"Andressa Melo da Fonseca",
"André Alcântara Aguiar",
"André Francisco Berenger de Araujo",
"Ariane Carvalho da Cruz",
"Arnaldo Lucas Pires Junior",
"Ayra Guedes Garrido",
"Barbara de Almeida Guimarães",
"Barbara Mangueira do Nascimento",
"Barbara Maria de Albuquerque Mitchell",
"Bernardo Moraes Ferreira Reis",
"Bruno Marinho de Matos",
"Bruno Rodrigo Couto Lemos",
"Camila Ferreira Figueiredo",
"Carla Teodoro Costa",
"Carlos Romário da Silva de Matos",
"Carolina Ferreira de Figueiredo",
"Carolina Mann de Oliveira",
"Carolina Perpétuo Corrêa",
"Caroline Rios Costa",
"Celia Daniele Moreira de Souza",
"Clarice Barros Araújo Berkowicz",
"Clemente Gentil Penna",
"Cleudiza Fernandes de Souza",
"Daniel Dutra Coelho Braga",
"Daniel Teixeira Taveira",
"Daniella Dalla Maestri",
"Denise da Silva de Oliveira",
"Diego de Moraes Campos",
"Diego Knack",
"Dominique Neves Pereira",
"Eduardo Henrique Sabioni Ribeiro",
"Eduardo Martins Jorge",
"Eduardo Santiago Couto",
"Eduardo Tude Falcão",
"Elaine Cristina Ventura Ferreira",
"Elion de Souza Campos",
"Emanuelly Gomes dos Santos Foppa",
"Felipe Bernardo da Silva Goebel",
"Fernanda Bana Arouca",
"Fernanda Coelho Mendes",
"Fernanda Coutinho Teixeira",
"Fernanda Gabrielly Terra Moura",
"Filipe Duret Athaide",
"Filipe Oliveira da Silva",
"Filipe Pitrosse",
"Gabriel Alves Pereira",
"Gabriel Felipe Oliveira de Mello",
"Gabriel Melo Mizrahi",
"Gabriel Pereira de Oliveira",
"Gabriela Machado do Amaral",
"Geison Siqueira Tavares da Cruz",
"Gilberto de Souza Vianna",
"Giovanna Zamith Cesário",
"Glauber de Oliveira Montes",
"Guilherme Leite Ribeiro",
"Gustavo Junqueira Costa Maia",
"Hendie Tavares Teixeira",
"Henrique Machado Vieira Lopes",
"Ingrid Gomes Ferreira",
"Isaac Carlos Trevisan da Costa",
"Isabela Frias Masi",
"Isabelle Cristina da Silva Pires",
"Jaime Mitropoulos",
"Janaína Di Lourenço Esteves",
"Jefferson dos Santos Alves",
"Jerônimo Aguiar Duarte da Cruz",
"Jonathan Cesar Rodrigues",
"Jorge Steimback Barbosa Junior",
"Josimar Faria Duarte",
"João Fernando Barreto de Brito",
"João Paulo Henrique Pinto",
"João Vitor de Oliveira Silva",
"Juliana Assis Nascimento",
"Jéssyca Silveira Souza",
"Júlio Dória",
"Kamila Gouveia Camargo Cré",
"Lays Correa da Silva",
"Leandro Arraes Liberali",
"Leandro César Santana Neves",
"Letícia Gomes do Nascimento",
"Letícia Helena de Oliveira",
"Luan Mendes de Medeiros Siqueira",
"Luca Araujo de Oliveira Leite",
"Lucas Vinicius Erichsen da Rocha",
"Luis Guilherme Eschenazi Lucena",
"Luiz Antonio da Silva Teixeira",
"Luiz Felipe Vieira Ferrão",
"Luiza das Neves Gomes",
"Luiza Nascimento de Oliveira da Silva",
"Luís Ricardo Araujo da Costa",
"Lívia Freitas Pinto Silva Soares",
"Maria Beatriz Gomes Bellens Porto",
"Maria Cristina Portella Ribeiro",
"Mariana Nastari Siqueira",
"Mariana Pastana Batista da Silva",
"Matheus Aguiar Duccini Ultra",
"Matheus Almeida Gonçalves Pereira",
"Matheus Brum Domingues Dettmann",
"Matheus Teixeira Moretti",
"Mayara de Freitas Portilho Silveira",
"Maíra Cristina Tomé Fonseca",
"Moisés Corrêa Fonseca da Silva",
"Moisés Peixoto Soares",
"Murillo Dias Winter",
"Mylena Pereira da Silva",
"Márcio de Oliveira Albuquerque",
"Mário Novaes César Rezende",
"Mônica Santos da Silva",
"Natasha Augusto Barbosa",
"Natasha Mastrangelo Silva de Moraes",
"Natália de Fátima de Carvalho Lacerda",
"Paola Vargas Arana",
"Patrícia Ramos Geremias",
"Paula Mello dos Santos",
"Paulo Francisco Donadio Baptista",
"Rachel Romano dos Santos",
"Rafael do Nascimento Souza Brasil",
"Rafaela Jacyczen laux",
"Raquel Marques Soares",
"Raíra da Cunha Nunes Abi-Ramia",
"Rebecca Hodesh Muniz de Souza Rozas",
"Renata da Silva Feliciano",
"Renata Dias Pinto Monteiro",
"Renato Dalcin de Carvalho",
"Ricardo Augusto Pereira",
"Rodrigo Fernandes Antunes Vieira",
"Rodrigo Franco da Costa",
"Rodrigo Maia Monteiro",
"Tereza Raquel dos Santos Rodrigues",
"Thalita Maciel Soares",
"Thayná Fuly Garcia",
"Thiago Figueiredo Martins",
"Thiago Groh de Mello Cesar",
"Thiago Luiz Turibio da Silva",
"Thiago Torres Medeiros da Silva",
"Thiago Vinícius Ferreira",
"Thompson Clímaco Alves",
"Tiago Gomes da Silva",
"Tony Espósito Gonçalves",
"Valéria Dorneles Fernandes",
"Vanderlei Marinho Costa",
"Vanessa de Mendonça Rodrigues dos Santos",
"Vicente Gil da Silva",
"Victor Luiz Alvares Oliveira",
"Victor Moraes Pereira Vianna",
"Victor Serebrenick",
"Vinner Stutz de Oliveira",
"Vinícius Patrocínio Pereira Costa",
"Vitor Guilherme Martins",
"Wagner Alcides de Souza",
"Willian Vidal Reis",
"Yasmin Getirana Gonçalves Vicente",
]
nomes_para_filtrar_mestrando = [
    "Alessandra Nóbrega Monteiro",
"Amanda De Carvalho Santos Lima",
"Amaro Jose de Souza Neto",
"Ana Beatriz Ferreira Marques",
"Antonio Daniel Correia de Araujo",
"Antonio Paiva Souto Maior",
"Ariadne Pires Barbosa",
"Augusto Cesar Oliveira Martins",
"Beatriz Weisheimer de Mendonça",
"Danielle Freire da Silva",
"Fabio de Mello Baptista",
"Felipe José Souza Fernandes da Silva",
"Fernanda Silva Monteiro Pinto",
"Gabriel Camejo Sampaio",
"Gabriel Duarte Evangelista da Silva",
"Gabriela Fernandes Petrungaro",
"Henrique Freire de Jesus",
"Inghrid da Costa Masullo Mendes",
"Isabella dos Santos Daiub",
"Isadora Silva Gomes",
"Isis Saraiva Leão Medina",
"Jean Pedro Silva de Sousa",
"Josemberg Pereira de Araújo",
"João Martins Pinheiro Dias Pereira",
"João Pedro Teixeira Ferreira Thimoteo",
"Juliana Batista",
"Kevin Wetter Pereira Lima",
"Larissa de Oliveira Farias",
"Lenilson Nóbrega da Silva de Oliveira",
"Luana Camila Da Silva Rosario",
"Luana Leão Rodrigues",
"Luca Araujo de Oliveira Leite",
"Lucas Barroso Rego",
"Lucas Mariel de Carvalho Carnaúba de Menezes",
"Lucas Souza Nascimento",
"Luiza de Paschoal Mohamed",
"Maria Eduarda de França Monteiro",
"Maria Vitória de Oliveira Cardoso",
"Mariana Barrozo Gonzalez",
"Mariana Madruga Bianchini",
"Matheus Butrucci Gomes",
"Matheus Paranhos Giolo Mezadri",
"Mayra Mendes Trocado",
"Murilo Rosa Garcias",
"Nathália Carvalho da Silveira Assed",
"Nicolle Sthefane de Oliveira Lima",
"Nicoly Goldschmidt Vitorino",
"Paulo Cesar Machado Farias Junior",
"Pedro Henrique Garcia Pinto de Araújo",
"Rafael Bezerra Targino",
"Rodrigo Pereira de Sousa",
"Samuel Barbosa Junior",
"Tadeu Alencar de Azevedo Sant Ana Lemos",
"Thaís Regina Cardoso Barbosa",
"Victor Brandão de Oliveira",
"Victor Lisboa da Fonseca Santos",
"Victória Ferreira Cunha",
"Vinícius Potrich de Souza Macedo Gonçalves",
"Vitória Luyza Cardoso Barbosa",
"Yeda Santos de Azambuja Montes",
"Ísis Carla Vieira Ferreira Coelho",
]
nomes_para_filtrar_doutorando = [
    "Alexandra Sablina do Nascimento Veras",
"Alexia de Santana Rosa",
"Alípio Pereira do Carmo",
"Amanda Guimarães da Silva",
"Ana Lectícia Felix Angelotti",
"Ana Paula Campos Barra",
"André Arioza Vargas",
"Angélica Paulillo Ferroni",
"Anne Caroline Santos Nunes",
"Antônio Pedro de Almeida Santos",
"Beatriz Monteiro Lemos",
"Bruna Aparecida Gomes Coelho",
"Bruno Azambuja Araujo",
"Bruno Martins de Castro",
"Bruno Sousa Silva Godinho",
"Bárbara Geromel Campanholo",
"Cainã Carneiro Gusmão",
"Caio Marcelo Cabral Vilanova",
"Camila de Oliveira Farias",
"Camille Ferreira Leandro",
"Carla Bianca Carneiro Amarante Correia",
"Caroline Cardoso Planinschek",
"Daiani da Silva Barbosa",
"David Durval Jesus Vieira",
"Deborah da Costa Fontenelle",
"Dhyan Ramayana Ramos Rodrigues",
"Dirson Fontes da Silva Sobrinho",
"Eraldo de Souza Leão Filho",
"Eric Fagundes de Carvalho",
"Felipe da Silva Barbosa",
"Gabriel Alencar e Souza",
"Gabriel Almeida Bizzo",
"Geisimara Soares Matos",
"Giovanna Zamith Cesário",
"Gustavo Monteiro de Rezende",
"Gustavo Souza de Deus da Silva",
"Hana Mariana da Cruz Ribeiro Costa",
"Helen da Silva Silveira",
"Iasmin Castro de Souza",
"Iolanda Chaves Ferreira de Oliveira",
"Isabella Loureiro Khaled Poppe",
"Isabella Santos Pinheiro",
"Isabella Villarinho Pereyra",
"Jefferson de Albuquerque Mendes",
"Julia Amaral Amato Moreira",
"Julia Soares Leite Lanzarini de Carvalho",
"Juliana Gonçalves de Oliveira Ferreira",
"Juliana Nascimento da Silva",
"Jônatan Coutinho da Silva de Oliveira",
"Keicy Salustiano da Silva",
"Kezia Wandressa da Costa Lima",
"Laís Morgado Marcoje",
"Lavinia Izidoro Martins",
"Livia Claro Pires",
"Lucas de Mattos Moura Fernandes",
"Lucas Lixa Victor Neves",
"Lucas Sampaio Costa Souza",
"Luciana Campos Batista",
"Luciana Lucia da Silva",
"Luciano Bastos Meron Neves",
"Luis Henrique Souza dos Santos",
"Maicon Mariano",
"Mariana Freitas de Andrade",
"Marina Salgado Pinto",
"Maristela Santana",
"Maya Moldes da Rocha Pereira",
"Michelle Alves Pinheiro de Oliveira",
"Michelle Caetano",
"Millena Souza Farias",
"Milleni Freitas Rocha",
"Mirella Soraya Pinheiro Rodrigues de Oliveira",
"Mylena Porto da Gama",
"Naiara Müssnich Rotta Gomes de Assunção",
"Natalia de Souza Miranda",
"Nathara Marriel Mariano",
"Nicolas Campelo Pinto de Oliveira",
"Nina Fernandes Cunha Galvao",
"Patrick Antunes Menezes",
"Paulo Celso Liberato Corrêa",
"Pedro Henrique da Silva Oriola Cardoso",
"Pedro Henrique Ferreira Danese Oliveira",
"Rafael Vieira da Cal",
"Renan Perozini Gomes Barrozo",
"Rodrigo Rocha da Cunha",
"Séfora Semíramis Sutil",
"Suane Felippe Soares",
"Talita de Jesus Noronha Sanchez",
"Tatiana Rodrigues Gama Russo",
"Thays Alves Rodrigues",
"Vanessa de Souza Vieira da Rocha"
]


# Adicionar a opção "Todos"
nomes_para_filtrar = ["Todos"] + nomes_para_filtrar
nomes_para_filtrar_mestrando = ["Todos"] + nomes_para_filtrar_mestrando
nomes_para_filtrar_doutorando = ["Todos"] + nomes_para_filtrar_doutorando
nomes_para_filtrar_egressos = ["Todos"] + nomes_para_filtrar_egressos

anos_para_filtrar = ["Todos", "2021", "2022", "2023", "2024"]

# Dicionário com os arquivos Excel separados por categoria e tipo
excel_files = {
    "Produção Bibliográfica Doutorandos": pd.ExcelFile("data/Producao_Bibliografica_Doutorandos.xlsx"),
    "Produção Bibliográfica Mestrandos": pd.ExcelFile("data/Producao_Bibliografica_Mestrandos.xlsx"),
    "Produção Bibliográfica Egressos": pd.ExcelFile("data/Producao_Bibliografica_Egressos.xlsx"),
    "Produção Técnica Doutorandos": pd.ExcelFile("data/Producao_tecnica_Doutorandos.xlsx"),
    "Produção Técnica Mestrandos": pd.ExcelFile("data/Producao_tecnica_Mestrandos.xlsx"),
    "Produção Técnica Egressos": pd.ExcelFile("data/Producao_tecnica_Egressos.xlsx"),
    "Produção Cultural Doutorandos": pd.ExcelFile("data/Producao_cultural_Doutorandos.xlsx"),
    "Produção Cultural Mestrandos": pd.ExcelFile("data/Producao_cultural_Mestrandos.xlsx"),
    "Produção Cultural Egressos": pd.ExcelFile("data/Producao_cultural_Egressos.xlsx"),
    "Bancas Doutorandos": pd.ExcelFile("data/Bancas_Doutorandos.xlsx"),
    "Bancas Egressos": pd.ExcelFile("data/Bancas_Egressos.xlsx"),
    "Eventos Doutorandos": pd.ExcelFile("data/Eventos_Doutorandos.xlsx"),
    "Eventos Mestrandos": pd.ExcelFile("data/Eventos_Mestrandos.xlsx"),
    "Eventos Egressos": pd.ExcelFile("data/Eventos_Egressos.xlsx"),
    "Orientações Doutorandos": pd.ExcelFile("data/orientações_Doutorandos.xlsx"),
    "Orientações Mestrandos": pd.ExcelFile("data/orientações_Mestrandos.xlsx"),
    "Orientações Egressos": pd.ExcelFile("data/orientações_Egressos.xlsx"),
}

dataframes = {}
for file_name, excel_file in excel_files.items():
    dataframes[file_name] = {}
    for sheet_name in excel_file.sheet_names:
        df = excel_file.parse(sheet_name)
        df = df.applymap(lambda x: x.replace('\n', '').replace('\t', '') if isinstance(x, str) else x)
        if 'Ano' in df.columns:
            df['Ano'] = df['Ano'].astype(str)
        dataframes[file_name][sheet_name] = df

# Criar os filtros na barra lateral
with st.sidebar:
    # Filtro de graduação
    graduacoes = ["Mestrando", "Doutorando", "Egresso"]
    graduacao_selecionada = st.multiselect(
        "Selecione a(s) formação acadêmica(s) para filtrar", 
        options=graduacoes  # Caso queira que "Todos" seja selecionado por padrão
    )

    # Define nomes disponíveis com base na graduação selecionada
    if not graduacao_selecionada:
        nomes_disponiveis = nomes_para_filtrar  # Considera "Todos" se nada for selecionado
    else:
        nomes_disponiveis = []
        if "Mestrando" in graduacao_selecionada:
            nomes_disponiveis.extend(nomes_para_filtrar_mestrando)
        if "Doutorando" in graduacao_selecionada:
            nomes_disponiveis.extend(nomes_para_filtrar_doutorando)
        if "Egresso" in graduacao_selecionada:
            nomes_disponiveis.extend(nomes_para_filtrar_egressos)

    # Adiciona a opção "Todos" à lista de nomes
    nomes_disponiveis = nomes_disponiveis
    nomes_selecionados = st.multiselect(
        "Selecione o(s) Nome(s) para filtrar", 
        options=nomes_disponiveis
    )

    # Se nenhum nome for selecionado, considera como "Todos"
    if not nomes_selecionados or "Todos" in nomes_selecionados:
        nomes_selecionados = list(nomes_disponiveis[1:])

    # Filtrar dataframes por graduação e nomes para obter anos disponíveis
    anos_disponiveis = set()
    for arquivo in excel_files.keys():
        for sheet, df in dataframes[arquivo].items():
            # Aplica o filtro de graduação
            if graduacao_selecionada != "Todos":
                if graduacao_selecionada == "Mestrando":
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_mestrando)]
                elif graduacao_selecionada == "Doutorando":
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_doutorando)]
                elif graduacao_selecionada == "Egresso":
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_egressos)]
            # Aplica o filtro de nomes
            if "Todos" not in nomes_selecionados:
                df = df[df['Nome Completo'].isin(nomes_selecionados)]
            anos_disponiveis.update(df['Ano'].unique())

    anos_disponiveis = sorted(list(anos_disponiveis))
    anos_disponiveis = ["Todos"] + anos_disponiveis
    anos_selecionados = st.multiselect(
        "Selecione o(s) Ano(s) para filtrar", 
        options=anos_disponiveis
    )

    # Se nenhum ano for selecionado, considera como "Todos"
    if not anos_selecionados or "Todos" in anos_selecionados:
        anos_selecionados = list(anos_disponiveis[1:])

    # Filtrar dataframes por graduação, nomes e anos para obter arquivos disponíveis
    arquivos_disponiveis = set()
    for arquivo in excel_files.keys():
        incluir_arquivo = False
        for sheet, df in dataframes[arquivo].items():
            # Se não houver graduação selecionada, não filtra por graduação
            if not graduacao_selecionada:  # Quando nenhum item é selecionado
                incluir_arquivo = True  # Inclui todos os arquivos

            # Aplica o filtro de graduação apenas se houver seleção
            if graduacao_selecionada:
                if "Mestrando" in graduacao_selecionada and 'Mestrandos' in arquivo:
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_mestrando)]
                    incluir_arquivo = True
                elif "Doutorando" in graduacao_selecionada and 'Doutorandos' in arquivo:
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_doutorando)]
                    incluir_arquivo = True
                elif "Egresso" in graduacao_selecionada and 'Egressos' in arquivo:
                    df = df[df['Nome Completo'].isin(nomes_para_filtrar_egressos)]
                    incluir_arquivo = True

            # Aplica o filtro de nomes
            if "Todos" not in nomes_selecionados:
                df = df[df['Nome Completo'].isin(nomes_selecionados)]

            # Aplica o filtro de anos
            if "Todos" not in anos_selecionados:
                df = df[df['Ano'].isin(anos_selecionados)]

            if not df.empty and incluir_arquivo:
                arquivos_disponiveis.add(arquivo)

    arquivos_disponiveis = sorted(list(arquivos_disponiveis))
    arquivos_selecionados = st.multiselect(
        "Selecione a(s) Produção(s) para filtrar", 
        options=arquivos_disponiveis
    )

    # Filtrar dataframes por graduação, nomes, anos e arquivos para obter as sheets disponíveis
    sheets_disponiveis = set()
    for arquivo in arquivos_selecionados:
        for sheet, df in dataframes[arquivo].items():
            # Aplica o filtro de nomes
            if "Todos" not in nomes_selecionados:
                df = df[df['Nome Completo'].isin(nomes_selecionados)]
            
            # Aplica o filtro de anos
            if "Todos" not in anos_selecionados:
                df = df[df['Ano'].isin(anos_selecionados)]
            
            if not df.empty:
                sheets_disponiveis.add(sheet)

    sheets_disponiveis = ["Todos"] + sorted(list(sheets_disponiveis))
    sheets_selecionadas = st.multiselect(
        "Selecione o(s) Trabalho(s) para filtrar", 
        options=sheets_disponiveis
    )

    # Se nenhuma sheet for selecionada, considera como "Todos"
    if not sheets_selecionadas or "Todos" in sheets_selecionadas:
        sheets_selecionadas = list(sheets_disponiveis[1:])

st.subheader("Distribuição por Categoria: ")

# Função para contar as linhas de acordo com os filtros de forma dinâmica
def contar_linhas(df, nomes_selecionados, anos_selecionados):
    if nomes_selecionados:
        df = df[df['Nome Completo'].isin(nomes_selecionados)]
    if anos_selecionados:
        df = df[df['Ano'].isin(anos_selecionados)]
    return len(df)

# Inicializar dicionário para contagens e definir arquivos e sheets a contar
arquivos_para_contar = []
for arquivo in excel_files.keys():
    if "Mestrando" in graduacao_selecionada and 'Mestrandos' in arquivo:
        arquivos_para_contar.append(arquivo)
    elif "Doutorando" in graduacao_selecionada and 'Doutorandos' in arquivo:
        arquivos_para_contar.append(arquivo)
    elif "Egresso" in graduacao_selecionada and 'Egressos' in arquivo:
        arquivos_para_contar.append(arquivo)
    elif not graduacao_selecionada:  # Se nenhuma graduação foi selecionada, inclui todos os arquivos
        arquivos_para_contar.append(arquivo)
sheets_para_contar = None if "Todos" in sheets_selecionadas or not sheets_selecionadas else sheets_selecionadas
cores = ['#EDD19C', '#B35C37', '#88540B', '#6B8E23', '#25395D', '#8B0000']

contagens = {}
total_contagens = 0  # Para armazenar o total geral

# Realizar contagem com base nos filtros aplicados
for arquivo in arquivos_para_contar:
    total_linhas = 0
    sheets = dataframes[arquivo]
    for sheet, df in sheets.items():
        # Verifica se deve filtrar as sheets ou contar todas
        if not sheets_para_contar or sheet in sheets_para_contar:
            linhas_contadas = contar_linhas(df, nomes_selecionados, anos_selecionados)
            total_linhas += linhas_contadas
            total_contagens += linhas_contadas  # Acumula no total geral
    contagens[arquivo] = total_linhas

# Exibir o gráfico de pizza atualizado
fig = px.pie(
    names=list(contagens.keys()), 
    values=list(contagens.values()),
    color_discrete_sequence=cores
)
fig.update_layout(
    legend=dict(
        font=dict(
            size=20,         # Tamanho da fonte da legenda
            color='#B35C37' 
        )
    ),
    plot_bgcolor='#F5F5DC',  # Cor de fundo do espaço do gráfico
    paper_bgcolor='#FFFFFF' 
)

fig.update_traces(textfont=dict(color='black', size=14, family='Arial', weight='bold'))  

st.plotly_chart(fig)

# Exibir o total de linhas no centro do layout
st.markdown(
    f"<h2 style='text-align: center; color: #B35C37;'>Total de Produções Acadêmicas: {total_contagens}</h2>",
    unsafe_allow_html=True
)


st.subheader("Total por ANO: ")


# Filtrar os anos selecionados
if "Todos" in anos_selecionados or not anos_selecionados:
    anos_filtrados = ["2021", "2022", "2023", "2024"]
else:
    anos_filtrados = anos_selecionados

# Filtrar os nomes selecionados
if "Todos" in nomes_selecionados or not nomes_selecionados:
    nomes_filtrados = nomes_para_filtrar[1:]  # Exclui "Todos" para contagem real
else:
    nomes_filtrados = nomes_selecionados

# Filtrar os arquivos selecionados
if "Todos" in arquivos_selecionados or not arquivos_selecionados:
    arquivos_filtrados = list(dataframes.keys())
else:
    arquivos_filtrados = arquivos_selecionados

# Filtrar as sheets selecionadas
sheets_filtradas = []
if "Todos" in sheets_selecionadas or not sheets_selecionadas:
    sheets_filtradas = None  # Marca para incluir todas as sheets dentro dos arquivos filtrados
else:
    sheets_filtradas = sheets_selecionadas

# Contagem de linhas por ano, nome, arquivo e sheet selecionados
contagens_por_ano = {ano: 0 for ano in anos_filtrados}
for arquivo, sheets in dataframes.items():
    if arquivo in arquivos_filtrados:  # Aplica filtro de arquivos
        for sheet, df in sheets.items():
            # Aplica o filtro de sheets, se não for "Todos"
            if sheets_filtradas is None or sheet in sheets_filtradas:
                # Aplica os filtros de ano e nome no DataFrame e conta as linhas correspondentes
                for ano in contagens_por_ano.keys():
                    if "Ano" in df.columns and "Nome Completo" in df.columns:
                        # Filtra o DataFrame usando todos os critérios
                        contagens_por_ano[ano] += len(df[(df['Ano'] == ano) & (df['Nome Completo'].isin(nomes_filtrados))])



fig_bar = px.bar(
    x=list(contagens_por_ano.keys()),
    y=list(contagens_por_ano.values())
)

# Atualizando as cores e estilos
fig_bar.update_traces(marker_color='#B35C37')  # Cor das barras
fig_bar.update_traces(text=list(contagens_por_ano.values()), textposition='outside')  # Rótulos de dados

# Definindo o eixo x como categórico e estilizando
fig_bar.update_xaxes(
    type='category',
    title_font=dict(color='black', size=16, family='Arial', weight='bold'),  # Título do eixo X
    tickfont=dict(color='black', size=14, family='Arial', weight='bold')  # Fonte dos ticks do eixo X
)

fig_bar.update_yaxes(
    title_font=dict(color='black', size=16, family='Arial', weight='bold'),  # Título do eixo Y
    tickfont=dict(color='black', size=14, family='Arial', weight='bold')  # Fonte dos ticks do eixo Y
)

# Atualizando o layout do gráfico
fig_bar.update_layout(
    plot_bgcolor='#FFFFFF',  # Cor de fundo do gráfico
    paper_bgcolor='#FFFFFF',  # Cor de fundo da área ao redor do gráfico
    font=dict(color='black', family='Arial')  # Cor do texto geral no gráfico
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_bar)

# Verificar se "Orientações" foi selecionado para exibir os gráficos de pizza
def exibir_graficos_orientacoes():
    andamento_contagens = {}
    concluida_contagens = {}
    total_andamento = 0
    total_concluida = 0

    # Definir cores fixas para cada categoria
    cores = ['#EDD19C', '#B35C37', '#88540B', '#6B8E23', '#25395D', '#8B0000']
    categorias = ["Categoria1", "Categoria2", "Categoria3", "Categoria4", "Categoria5", "Categoria6"]
    color_map = {categoria: cor for categoria, cor in zip(categorias, cores)}

    # Contar "Andamento" e "Concluída" em cada sheet
    for sheet, df in dataframes["Orientações"].items():
        if "andamento" in sheet.lower():
            andamento_contagens[sheet] = contar_linhas(df, nomes_selecionados, anos_selecionados)
            total_andamento += andamento_contagens[sheet]
        elif "concluida" in sheet.lower():
            concluida_contagens[sheet] = contar_linhas(df, nomes_selecionados, anos_selecionados)
            total_concluida += concluida_contagens[sheet]

    # Gráfico de pizza para "Andamento"
    fig_andamento = px.pie(
        names=list(andamento_contagens.keys()), 
        values=list(andamento_contagens.values()),
        color=list(andamento_contagens.keys()),  # Definindo cores com base nas chaves
        color_discrete_map=color_map,
        title="Orientações em Andamento"
    )
    
    # Aplicando layout e estilos ao gráfico de pizza "Em Andamento"
    fig_andamento.update_layout(
        legend=dict(
            font=dict(
                size=20,         # Tamanho da fonte da legenda
                color='#B35C37'  # Cor da fonte da legenda
            )
        ),
        plot_bgcolor='#F5F5DC',  # Cor de fundo do espaço do gráfico
        paper_bgcolor='#FFFFFF'   # Cor de fundo da área ao redor do gráfico
    )

    fig_andamento.update_traces(textfont=dict(color='black', size=14, family='Arial', weight='bold'))  # Estilo dos rótulos de dados

    # Gráfico de pizza para "Concluída"
    fig_concluida = px.pie(
        names=list(concluida_contagens.keys()), 
        values=list(concluida_contagens.values()),
        color=list(concluida_contagens.keys()),  # Definindo cores com base nas chaves
        color_discrete_map=color_map,
        title="Orientações Concluídas"
    )

    # Aplicando layout e estilos ao gráfico de pizza "Concluída"
    fig_concluida.update_layout(
        legend=dict(
            font=dict(
                size=20,         # Tamanho da fonte da legenda
                color='#B35C37'  # Cor da fonte da legenda
            )
        ),
        plot_bgcolor='#F5F5DC',  # Cor de fundo do espaço do gráfico
        paper_bgcolor='#FFFFFF'   # Cor de fundo da área ao redor do gráfico
    )

    fig_concluida.update_traces(textfont=dict(color='black', size=14, family='Arial', weight='bold'))  # Estilo dos rótulos de dados

    st.subheader("Distribuição de Orientações: ")
     # Mostrar os gráficos lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_andamento)
    with col2:
        st.plotly_chart(fig_concluida)
# Verificar se "Orientações" foi selecionado para exibir os gráficos de pizza
if "Orientações" in arquivos_selecionados:
    exibir_graficos_orientacoes()
#else:
#    st.subheader("Selecione 'Orientações' no Filtro para visualizar os gráficos de andamento e concluídas.")

# Exibir a tabela da primeira sheet selecionada, se houver
if sheets_selecionadas:
    sheet_selecionada = sheets_selecionadas[0]  # Pega apenas a primeira sheet selecionada
    for arquivo in arquivos_selecionados:
        if sheet_selecionada in dataframes[arquivo]:
            df_sheet = dataframes[arquivo][sheet_selecionada]

            # Aplicar filtros de nome e ano, se selecionados
            if nomes_selecionados and "Todos" not in nomes_selecionados:
                df_sheet = df_sheet[df_sheet['Nome Completo'].isin(nomes_selecionados)]
            if anos_selecionados and "Todos" not in anos_selecionados:
                df_sheet = df_sheet[df_sheet['Ano'].isin(anos_selecionados)]

            # Ordenar pela coluna "Ano" se ela estiver presente
            if 'Ano' in df_sheet.columns:
                df_sheet = df_sheet.sort_values(by='Ano', ascending=False)

            # Exibir a tabela no Streamlit com barra de rolagem
            st.subheader(f"Tabela de Dados: {sheet_selecionada} - {arquivo}")

            # Gerar HTML da tabela e aplicar estilo
            tabela_html = df_sheet.to_html(index=False)  # Converte DataFrame para HTML sem índice
            tabela_html = tabela_html.replace('<table', '<table style="border-collapse: collapse; border: 2px solid #B35C37;"')
            tabela_html = tabela_html.replace('<th', '<th style="border: 2px solid #B35C37; color: #B35C37;"')
            tabela_html = tabela_html.replace('<td', '<td style="border: 2px solid #B35C37;"')
            st.markdown(
                f"""
                <div style="overflow-x: auto; color: #B35C37;">
                    {tabela_html}
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.subheader("Nenhum Trabalho selecionado para exibir: ")












