import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def generate_random_number():
    return random.randint(1, 100)

@app.route('/')
def index():
    return '''
   <!DOCTYPE html>
<html>
<head>
    <title>🎲 Gerador de Números Mágicos</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            animation: gradientShift 8s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            50% { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
            100% { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 400px;
            width: 90%;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        h1 {
            color: #4a4a4a;
            font-size: 2.5em;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: rainbow 3s ease-in-out infinite alternate;
        }
        
        @keyframes rainbow {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }
        
        .dice-icon {
            font-size: 3em;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        
        button {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 30px;
        }
        
        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
            background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        #result {
            font-size: 24px;
            color: #333;
            margin-top: 20px;
            min-height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .number {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            padding: 10px 20px;
            border-radius: 15px;
            font-size: 2em;
            font-weight: bold;
            margin-left: 10px;
            animation: pulse 0.6s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        @keyframes pulse {
            0% { transform: scale(0.5); opacity: 0; }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); opacity: 1; }
        }
        
        .sparkle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #FFD700;
            border-radius: 50%;
            animation: sparkle 1.5s linear infinite;
        }
        
        @keyframes sparkle {
            0% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
            100% { opacity: 0; transform: scale(0); }
        }
        
        .subtitle {
            color: #666;
            font-size: 1.1em;
            margin-bottom: 20px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="dice-icon">🎲</div>
        <h1>Gerador Mágico</h1>
        <p class="subtitle">Descubra seu número da sorte!</p>
        <button onclick="generateNumber()">✨ Gerar Número ✨</button>
        <div id="result"></div>
    </div>
    
    <script>
        function generateNumber() {
            // Adiciona efeito de loading
            document.getElementById('result').innerHTML = '🎯 Gerando...';
            
            // Cria efeito de partículas
            createSparkles();
            
            setTimeout(() => {
                fetch('/generate')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = 
                            `Seu número é: <span class="number">${data.number}</span>`;
                    })
                    .catch(error => {
                        document.getElementById('result').innerHTML = 
                            'Ops! Algo deu errado 😅';
                    });
            }, 800);
        }
        
        function createSparkles() {
            const container = document.querySelector('.container');
            for (let i = 0; i < 10; i++) {
                const sparkle = document.createElement('div');
                sparkle.className = 'sparkle';
                sparkle.style.left = Math.random() * 100 + '%';
                sparkle.style.top = Math.random() * 100 + '%';
                sparkle.style.animationDelay = Math.random() * 1.5 + 's';
                container.appendChild(sparkle);
                
                setTimeout(() => {
                    sparkle.remove();
                }, 1500);
            }
        }
        
        // Efeito de loading na página
        window.addEventListener('load', () => {
            document.querySelector('.container').style.animation = 'fadeIn 0.8s ease';
        });
    </script>
    
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</body>
</html>

    '''

@app.route('/generate')
def generate():
    return jsonify({'number': generate_random_number()})

if __name__ == '__main__':
    app.run(debug=True)
