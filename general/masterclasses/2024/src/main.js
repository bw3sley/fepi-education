const questions = [
    {
      question: "Qual é o uso do operador '===' em JavaScript?",
      answers: [
        "Atribuição de valor",
        "Comparação de valor e tipo",
        "Adição de valores"
      ],
      right: 1
    },
    {
      question: "Qual método é usado para analisar uma string para um inteiro em JavaScript?",
      answers: [
        "parseInt()",
        "parseString()",
        "toInt()"
      ],
      right: 0
    },
    {
      question: "Qual palavra-chave é usada para definir uma variável em JavaScript?",
      answers: [
        "var",
        "let",
        "Ambas 'var' e 'let'"
      ],
      right: 2
    },
    {
      question: "Qual objeto é a base de todos os objetos em JavaScript?",
      answers: [
        "Object",
        "Array",
        "String"
      ],
      right: 0
    },
    {
      question: "Qual função é usada para escrever algo no console do navegador?",
      answers: [
        "document.write()",
        "console.write()",
        "console.log()"
      ],
      right: 2
    },
    {
      question: "Como você declara uma função em JavaScript?",
      answers: [
        "function:myFunction()",
        "function myFunction()",
        "var myFunction = function()"
      ],
      right: 1
    },
    {
      question: "Qual método remove o último elemento de um array em JavaScript?",
      answers: [
        "pop()",
        "push()",
        "last()"
      ],
      right: 0
    },
    {
      question: "Qual operador é usado para verificar se dois valores são iguais em valor em JavaScript?",
      answers: [
        "==",
        "===",
        "="
      ],
      right: 0
    },
    {
      question: "Como você pode adicionar um comentário em uma linha em JavaScript?",
      answers: [
        "// Comentário",
        "/* Comentário */",
        "<!-- Comentário -->"
      ],
      right: 0
    },
    {
      question: "Qual estrutura de repetição é usada para executar um bloco de código um número específico de vezes?",
      answers: [
        "for",
        "while",
        "do-while"
      ],
      right: 0
    },
  ];
  
  const quiz = document.querySelector("#quiz");
  
  const template = document.querySelector("template");
  
  const rightAnswers = new Set();
  
  const totalQuestions = questions.length;
  
  const showRightAnswers = document.querySelector("#right-answers span");
  
  showRightAnswers.textContent = `${rightAnswers.size} de ${totalQuestions}`;
  
  for (const item of questions) {
    const quizItem = template.content.cloneNode(true);
  
    quizItem.querySelector("h3").textContent = item.question;
  
    for (const answer of item.answers) {
      const dt = quizItem.querySelector("dl dt").cloneNode(true);
  
      dt.querySelector("label").textContent = answer;
  
      dt.querySelector("input").setAttribute("name", `question-${questions.indexOf(item)}`);
      dt.querySelector("input").value = item.answers.indexOf(answer);
  
      dt.querySelector("input").onchange = (event) => {
        const isRight = Number(event.target.value) === item.right;
  
        rightAnswers.delete(item);
  
        if (isRight) {
          rightAnswers.add(item);
        }
  
        showRightAnswers.textContent = `${rightAnswers.size} de ${totalQuestions}`;
      }
  
      quizItem.querySelector("dl").appendChild(dt);
    }
  
    quizItem.querySelector("dl dt").remove();
  
    quiz.appendChild(quizItem);
  }