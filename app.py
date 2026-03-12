import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print(">>> ERROR: No se encontró la GEMINI_API_KEY en el archivo .env")
    exit()

client = genai.Client(api_key=api_key)

def tutor_virtual():
    print("   BIENVENIDO AL TUTOR VIRTUAL DE ENFERMERIA PARA ESTUDIANTES")
    
    nombre_usuario = input("por favor ingrese su nombre: ")
    print("Conectando con la base de datos de aprendizaje")
    print(f"Sesión iniciada para: {nombre_usuario}\n")

    while True:
        tema = input("¿Qué concepto quieres estudiar hoy? (o escribe 'salir'): ")
        
        if tema.lower() == 'salir':
            print("\n[SISTEMA]: Guardando progreso... ¡Hasta pronto!")
            break

        if not tema.strip():
            continue

        try:
            print(f"\nEstoy analizando '{tema}'... Por favor, espera.")
            
            # Usamos el modelo gemini-2.5-flash según tu panel de control
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""Actúa como un tutor experto en enfermería. 
                Explica de forma clara, pedagógica y profesional el siguiente concepto: {tema}"""
            )
            
            print("\n" + "="*20)
            print("   Explicaccion del tutor")
            print("="*20)
            print(response.text)
            print("="*40)
            
            # Simulación de registro de actividad técnica
            print(f"\n[INFO]: Concepto '{tema}' registrado en tu historial.")
            print(f"[INFO]: Generando recomendaciones de repaso...\n")

        except Exception as e:
            print(f"\n>>> Error técnico: {e}")
            if "429" in str(e):
                print("Sugerencia: Has alcanzado el límite de frecuencia, espera 15 segundos.")
            break

if __name__ == "__main__":
    tutor_virtual()