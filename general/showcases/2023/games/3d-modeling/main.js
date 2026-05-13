const form = document.querySelector("form");
const inputs = document.querySelectorAll("input[type='radio']");
const button  = document.querySelector("button[type='submit']");

for (const input of inputs) {
    input.addEventListener("click", () => {
        const checkedInputs = document.querySelectorAll("input[type='radio']:checked");
        
        if (checkedInputs.length === 5) {
            button.removeAttribute("disabled");
        } 
        
        else {
            button.setAttribute("disabled", "disabled");
        }
    });
}

const rightAnswers = [
    {
        id: "question-1",
        answer: "entry"
    },
    {
        id: "question-2",
        answer: "entry"
    },
    {
        id: "question-3",
        answer: "entry"
    },
    {
        id: "question-4",
        answer: "4"
    },
    {
        id: "question-5",
        answer: "2"
    }
];

form.onsubmit = (event) => {
    event.preventDefault();

    const userAnswers = [];

    const answers = document.querySelectorAll("input[type='radio']:checked");

    for (const answer of answers) {
        const selectedQuestion =  answer.name;
        const selectedAnswer = answer.value;

        const rightQuestion = rightAnswers.find(question => question.id === selectedQuestion);

        if (rightQuestion.answer === selectedAnswer) {
            userAnswers.push(selectedAnswer);
        }

        else {
            answer.parentElement.classList.add("wrong-answer");
        }
    }

    document.querySelector("#final-answer").classList.remove("hidden");
    document.querySelector("#final-question").classList.remove("hidden");

    const wrapper = document.querySelector("#final-message");

    const strong = document.createElement("strong");
    const p = document.createElement("p");
    const reloadButton = document.createElement("button");
    
    strong.classList.add("text-2xl");

    reloadButton.type = "button";
    reloadButton.classList.add("reload-button");
    reloadButton.innerHTML = `<i class="ph-fill ph-arrow-clockwise"></i> Tentar novamente`;

    if (userAnswers.length === 5) {
        strong.textContent = "Parabéns! Você acertou todas as questões! 🎉👏";

        p.textContent = "Você é realmente incrível e demonstrou um conhecimento impressionante. Continue assim e continue se desafiando. Continue com esse espírito vencedor! Para retirar seu brinde, tire uma foto do placar, poste em seu Instagram marcando @fepi.siads e mostre para algum aluno.";
    }

    else if (userAnswers.length >= 1 && userAnswers.length <= 4) {
        strong.textContent = `Parabéns! Você acertou entre ${userAnswers.length} e 5 questões! 🎉`;

        p.textContent = "Isso mostra que você tem um bom conhecimento e habilidades. Continue praticando e estudando para melhorar ainda mais. Cada acerto é um passo na direção certa, e você está no caminho certo para o sucesso. Continue assim! Para retirar seu brinde, tire uma foto do placar, poste em seu Instagram marcando @fepi.siads e mostre para algum aluno.";
    }

    else {
        strong.textContent = "Você não acertou nenhuma questão, porém não desanime! Às vezes, errar é apenas um passo em direção ao sucesso";

        p.textContent = "Mesmo que você não tenha acertado nenhuma questão neste quiz, lembre-se de que é uma oportunidade de aprender e melhorar. Use isso como motivação para estudar mais e se preparar melhor da próxima vez. O importante é continuar tentando e nunca desistir. Seu esforço será recompensado, e você certamente vai progredir. Você pode refazer o quiz para conseguir seu brinde.";
    }

    wrapper.append(strong, p, reloadButton);

    button.setAttribute("disabled", true);

    reloadButton.addEventListener("click", (event) => location.reload())

    wrapper.scrollIntoView();
};