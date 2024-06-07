import tkinter as tk
from tkinter import ttk
import webbrowser

# Função para criar um dicionário com as informações de poluição de uma praia
def criar_informacoes_poluicao(estado, nivel_poluicao, causa_poluicao, especies_afetadas, em_reparo, link_local):
    return {
        "estado": estado,
        "nivel_poluicao": nivel_poluicao,
        "causa_poluicao": causa_poluicao,
        "especies_afetadas": especies_afetadas,
        "em_reparo": em_reparo,
        "link_local": link_local
    }

# Função para obter informações de poluição para uma determinada área
def obter_informacoes_poluicao(banco_dados, local):
    return banco_dados.get(local)

# Dicionário contendo informações sobre poluição em diferentes praias
banco_dados = {
    "Barra da Tijuca": criar_informacoes_poluicao("Rio de Janeiro", "Moderado", "Descarte inadequado de resíduos", ["Tartaruga", "Golfinho"], True, "https://www.google.com/maps/place/Barra+da+Tijuca,+Rio+de+Janeiro+-+RJ/@-23.0098023,-43.523531,12z/data=!3m1!4b1!4m14!1m7!3m6!1s0x9bc2cdead0f623:0x618a0cca0ad51256!2sPraia+da+Barra+da+Tijuca!8m2!3d-23.013023!4d-43.3200848!16s%2Fg%2F11bxg1nqh2!3m5!1s0x9bda4a27b6fe5d:0x63c3f6d1d89e0f4e!8m2!3d-23.0040194!4d-43.3661069!16s%2Fg%2F11b76h6hc0?entry=ttu"),
    "Ilhabela": criar_informacoes_poluicao("São Paulo", "Leve", "Vazamento de óleo", ["Peixe", "Gaivota"], False, "https://www.google.com/maps/place/Ilhabela,+SP/@-23.8022044,-45.4463548,13z/data=!3m1!4b1!4m6!3m5!1s0x94d299a1e1b58951:0xdb1cb1ae3f4ba322!8m2!3d-23.8165908!4d-45.3667925!16zL20vMDJ5Zjlw?entry=ttu"),
    "Santos": criar_informacoes_poluicao("São Paulo", "Severo", "Despejo de esgoto", ["Caranguejo", "Lontra"], True, "https://www.google.com/maps/place/Santos,+SP/@-23.9549098,-46.3868866,13z/data=!3m1!4b1!4m6!3m5!1s0x94ce03423c3b1c3b:0x584dceedfc63644f!8m2!3d-23.9592038!4d-46.3317806!16s%2Fg%2F120hthm_?entry=ttu"),
    "Boa Viagem": criar_informacoes_poluicao("Recife", "Moderado", "Poluição industrial", ["Peixe", "Tubarão"], False, "https://www.google.com/maps/place/Boa+Viagem,+Recife+-+PE/@-8.1268839,-34.939716,14z/data=!3m1!4b1!4m6!3m5!1s0x7ab1fb60ecfb19b:0xb442389feeea73be!8m2!3d-8.1317303!4d-34.902409!16s%2Fm%2F026k0jd?entry=ttu"),
    "Ondina": criar_informacoes_poluicao("Bahia", "Leve", "Descarte de plásticos", ["Tartaruga", "Gaivota"], True, "https://www.google.com/maps/place/Ondina,+Salvador+-+BA/@-13.0044514,-38.5202677,15z/data=!4m6!3m5!1s0x7160361b6858881:0xa56066918d886e19!8m2!3d-13.0059432!4d-38.5092502!16s%2Fg%2F11bc688qsl?entry=ttu"),
    "Redinha": criar_informacoes_poluicao("Rio Grande do Norte", "Leve", "Despejo de resíduos químicos", ["Peixe", "Caranguejo"], False, "https://www.google.com/maps/place/Redinha,+Natal+-+RN/@-5.7477246,-35.2572956,14z/data=!3m1!4b1!4m6!3m5!1s0x7b300a"),
    "Maragogi": criar_informacoes_poluicao("Alagoas", "Moderado", "Agricultura intensiva", ["Polvo", "Tubarão"], True, "https://www.google.com/maps/place/Maragogi,+AL,+57955-000/@-9.0166067,-35.2430018,14z/data=!3m1!4b1!4m6!3m5!1s0x700f54d6c7b13db:0x7a5d839403b9f392!8m2!3d-9.0127163!4d-35.2213954!16s%2Fg%2F11bxfw8p15?entry=ttu"),
    "Tubarao": criar_informacoes_poluicao("Santa Catarina", "Severo", "Vazamento de óleo", ["Peixe", "Gaivota"], False, "https://www.google.com/maps/place/Tubar%C3%A3o,+SC/@-28.4719247,-49.0939703,13z/data=!3m1!4b1!4m6!3m5!1s0x952142592ca52293:0xf8e8b689980101de!8m2!3d-28.4818875!4d-49.0058727!16s%2Fg%2F11bc6myq4p?entry=ttu"),
    "Lagoa da Conceicao": criar_informacoes_poluicao("Santa Catarina", "Leve", "Turismo descontrolado", ["Caranguejo", "Lontra"], True, "https://www.google.com/maps/place/Lagoa+da+Concei%C3%A7%C3%A3o,+Florian%C3%B3polis+-+SC/@-27.6038933,-48.4837646,15z/data=!3m1!4b1!4m6!3m5!1s0x95273ea848636a4d:0x6f700ac19098c89d!8m2!3d-27.603092!4d-48.4712296!16s%2Fg%2F11bxg0dj8s?entry=ttu"),
    "Guaratuba": criar_informacoes_poluicao("Paraná", "Moderado", "Pesca predatória", ["Peixe", "Gaivota"], False, "https://www.google.com/maps/place/Guaratuba,+PR,+83280-000/@-25.9173315,-48.6737335,12z/data=!3m1!4b1!4m6!3m5!1s0x94dbfaa3c88e2f1d:0x523ba0a71acc2a73!8m2!3d-25.8843865!4d-48.5762979!16s%2Fm%2F026_tf4?entry=ttu")
}

# Função para exibir informações de poluição de uma praia selecionada
def exibir_informacoes_poluicao(praia):
    informacoes_poluicao = obter_informacoes_poluicao(banco_dados, praia)
    if informacoes_poluicao:
        info_text.set(
            f"Informações sobre a área {praia}:\n"
            f"Estado: {informacoes_poluicao['estado']}\n"
            f"Nível de Poluição: {informacoes_poluicao['nivel_poluicao']}\n"
            f"Causa da Poluição: {informacoes_poluicao['causa_poluicao']}\n"
            f"Animais Afetados: {', '.join(informacoes_poluicao['especies_afetadas'])}\n"
            f"Status da Praia: {'Está em reparação' if informacoes_poluicao['em_reparo'] else 'Não está em reparação'}\n"
            f"Localização do Maps: {informacoes_poluicao['link_local']}"
        )
        link_button.config(state=tk.NORMAL)
    else:
        info_text.set("Área não encontrada. Por favor, tente novamente.")
        link_button.config(state=tk.DISABLED)

# Função para abrir o link do Google Maps no navegador padrão
def abrir_link():
    praia = praia_var.get()
    informacoes_poluicao = obter_informacoes_poluicao(banco_dados, praia)
    if informacoes_poluicao:
        webbrowser.open(informacoes_poluicao['link_local'])

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Informações sobre Poluição nas Praias")

# Variável para armazenar a seleção da praia
praia_var = tk.StringVar()

# Criação do menu de seleção (Dropdown)
praia_label = ttk.Label(root, text="Selecione uma praia:")
praia_label.pack(pady=10)

praia_dropdown = ttk.Combobox(root, textvariable=praia_var)
praia_dropdown['values'] = ["Barra da Tijuca", "Ilhabela", "Santos", "Boa Viagem", "Ondina", "Redinha", "Maragogi", "Tubarao", "Lagoa da Conceicao", "Guaratuba"]
praia_dropdown.pack(pady=10)
praia_dropdown.bind("<<ComboboxSelected>>", lambda e: exibir_informacoes_poluicao(praia_var.get()))

# Texto para exibir informações sobre a praia selecionada
info_text = tk.StringVar()
info_label = ttk.Label(root, textvariable=info_text, justify=tk.LEFT)
info_label.pack(pady=10)

# Botão para abrir o link do Google Maps
link_button = ttk.Button(root, text="Abrir no Google Maps", command=abrir_link, state=tk.DISABLED)
link_button.pack(pady=10)

# Inicia a interface gráfica
root.mainloop()