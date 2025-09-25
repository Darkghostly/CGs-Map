Mapa de Expansão e Análise Geográfica
Este projeto é uma ferramenta de visualização de dados geoespaciais projetada para análises de negócio. Ele gera um mapa HTML interativo a partir de um conjunto de dados JSON, permitindo mapear e analisar pontos de operação, áreas de influência e potenciais locais de expansão para uma empresa.

O sistema é ideal para equipes de inteligência de mercado, planejamento estratégico e logística que precisam de uma visão clara e customizável de suas operações no terreno.

(Sugestão: Gere um mapa, tire um screenshot e coloque-o em uma pasta docs/ para referência visual)

✨ Funcionalidades Principais
Mapa Interativo: Gera um arquivo HTML autônomo que não requer um servidor web para funcionar.

Múltiplas Camadas: Permite alternar entre uma visão de mapa esquemática ("Tática") e imagens de satélite de alta resolução.

Áreas de Influência: Visualiza um raio de atuação ou influência customizável para cada ponto no mapa.

Informações Detalhadas: Exibe informações específicas de cada ponto através de pop-ups interativos ao clicar nos marcadores.

Visualização de Dependências: Permite traçar linhas entre os pontos para representar fluxos logísticos, dependências ou outras relações.

🛠️ Tecnologias Utilizadas
Python 3

Folium para a geração dos mapas interativos.

🚀 Instalação e Configuração
Para executar este projeto localmente, siga os passos abaixo.

Clone o Repositório

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e Ative um Ambiente Virtual

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no Linux / macOS
source venv/bin/activate
Instale as Dependências
O projeto tem poucas dependências, listadas no arquivo requirements.txt. Para instalá-las, execute:

Bash

pip install -r requirements.txt
📈 Como Usar
Edite os Dados de Entrada
Abra o arquivo data/centros_gravidade.json. Este arquivo contém a lista de pontos que serão exibidos no mapa. Adicione, remova ou modifique os objetos JSON para refletir os dados da sua empresa. Veja a seção Estrutura de Dados abaixo para mais detalhes.

Execute o Script de Geração
Com o ambiente virtual ativado, execute o script principal para gerar o mapa:

Bash

python main.py
Visualize o Resultado
Após a execução, um novo arquivo será criado em output/mapa_tatico_cg.html. Abra este arquivo em qualquer navegador web (Chrome, Firefox, etc.) para ver e interagir com seu mapa customizado.

📊 Estrutura de Dados
Para adicionar seus próprios pontos, edite o arquivo data/centros_gravidade.json. Ele é uma lista de objetos, onde cada objeto representa um ponto no mapa e deve seguir a estrutura abaixo:

Chave	Tipo	Descrição	Exemplo
nome	String	O nome do ponto de interesse (Ex: Sede, Filial, Centro de Distribuição).	"Porto de Santos"
tipo	String	A categoria ou tipo do ponto.	"Logística/Econômico"
coord	Array (Float)	As coordenadas geográficas no formato [latitude, longitude].	[-23.96, -46.30]
vulnerabilidade	Integer	Um índice de 0 a 100. Pode ser usado para representar prioridade, risco ou potencial.	70
impacto	String	Descrição do impacto estratégico ou da função do ponto.	"Interrupção de 40% do fluxo..."
cor	String	A cor do marcador no mapa (Ex: "red", "blue", "green", "orange").	"orange"
raio_influencia	Integer	O raio da área de influência em metros.	20000

Exportar para as Planilhas
🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para reportar bugs ou sugerir novas funcionalidades. Se desejar contribuir com código, por favor, abra um Pull Request.

📄 Licença
Este projeto está licenciado sob a Licença MIT.
