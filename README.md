# Proyecto 8: LLM
tutor virtual de enfermeria: este proyexto es un tutor inteligenete diseñado para asistir a estudiantes de enfermeria en el aprendizaje de conceptos, como farmacologia, anatomia y cuidados clinicos, como no tengo version gratuita de open ai utilice gemini 2.5 flash para realizar las explicaciones, este proyecto lo realice en base a mi anterior carrera de enfermria ya que tambien soy licenciado en enfermeria y querria realizar algo acorde a mi anterior carrera.
 
 Caracteristicas princiáles
 ia especializada: configure el system prompt orienteado a la eduacion de enfermeria
 simulacion: sistema de inicio de sesion de usuario e historial de aprendizaje


Escribe un instructivo de cómo podemos utilizar tu software (incluye instrucciones para crear entorno virtual)
primer paso, clonar el repositario: git clone https://github.com/solidsaul96/llm.git
cd llm

segundo paso: crear y activar el entorno virtual: 
py -3.12 -m venv .venv
.\.venv\Scripts\activate

tercer paso: instalar dependencias: pip install -r requirements.txt

cuarto paso: crea un archivo .env en la raiz del proyecto y añadi tu api key de google ai studio 
GEMINI_API_KEY=tu_clave_aqui
