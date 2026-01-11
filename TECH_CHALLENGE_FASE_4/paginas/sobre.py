import streamlit as st

def show():
    st.title("Sobre o Time 2")
    st.write("Conheça os membros do nosso time abaixo:")

    # Definindo informações sobre cada membro
    team_members = [{  "name": "Emily da Silva Vaculik",
            "photo": "https://media.licdn.com/dms/image/D4D03AQFS8a2Sq03t6g/profile-displayphoto-shrink_200_200/0/1675709544684?e=1726704000&v=beta&t=5fAhzltzhBUKt033mi6v6AxziucbenFO8qAwW5Z0EuA",  
            "graduation": "Engenheira de Alimentos - Faculdade de Tecnologia Termomecanica",
            "description":"Gerente de Contas Externas",
            "linkedin": "https://www.linkedin.com/in/emily-vaculik-9a82ab202/"
        },
        {  "name": " Marcos Barbosa da Silva",
           "photo": " https://media.licdn.com/dms/image/D4D03AQF26Tn_uiB3FQ/profile-displayphoto-shrink_200_200/0/1686167990179?e=1726704000&v=beta&t=0y-GrK0h0W9n7XD6wXl_EGrL4mJ-YTdShRtgTkw1WhE", 
           "graduation": " Administração de Empresas - Faculdade Impacta Tecnologia",
           "description":" Business Intelligence Sr",
           "linkedin": "https://www.linkedin.com/in/marcos-silva-61705b31/"},
        {
            "name": "Leandro Soares da Silva",
            "photo": "https://media.licdn.com/dms/image/D4D03AQGGp3NG8HiDxA/profile-displayphoto-shrink_800_800/0/1712980770530?e=1726704000&v=beta&t=cwv9AVlch64rCMOmvdBkH7WmgVhNaBGQz4KdfShcD-Q",  # Caminho para a foto do Leandro
            "graduation": "Bacharel em Engenharia de Computação",
            "description": "Analista de BI",
            "linkedin": "https://www.linkedin.com/in/leandro"
        },
    ]

    # Exibindo informações sobre cada membro
    for member in team_members:
        st.subheader(member["name"])
        st.image(member["photo"], width=150)
        st.write(member["description"])
        st.write(f"[LinkedIn]({member['linkedin']})")
        st.markdown("---")

