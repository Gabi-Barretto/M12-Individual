import os
from bark import generate_audio

# Diretórios para textos e áudios (caminho corrigido)
TEXTS_DIR = os.path.join(os.path.dirname(__file__), './texts')
AUDIOS_DIR = os.path.join(os.path.dirname(__file__), './audios')

# Verificar se o diretório de textos existe
if not os.path.exists(TEXTS_DIR):
    raise FileNotFoundError(f"Diretório de textos não encontrado: {TEXTS_DIR}")

# Criar diretório para áudios, se não existir
os.makedirs(AUDIOS_DIR, exist_ok=True)

# Função para gerar áudio de um texto
def generate_audio_from_text(text_file, audio_file):
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read().strip()
    print(f"Gerando áudio para: {text}")
    audio_array = generate_audio(text)
    # Certifique-se que o método correto de exportação está sendo usado
    audio_array.export(audio_file, format="wav")

# Iterar pelos arquivos de texto no diretório de textos
for text_file in os.listdir(TEXTS_DIR):
    if text_file.endswith(".txt"):
        text_path = os.path.join(TEXTS_DIR, text_file)
        audio_name = text_file.replace(".txt", ".wav")
        audio_path = os.path.join(AUDIOS_DIR, audio_name)
        generate_audio_from_text(text_path, audio_path)

print("Todos os áudios foram gerados com sucesso!")
