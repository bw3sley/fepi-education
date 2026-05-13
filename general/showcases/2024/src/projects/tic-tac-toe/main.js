const X_CLASS = "x";
const CIRCLE_CLASS = "circle";

const WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

const cells = document.querySelectorAll("[data-cell]");
const board = document.querySelector("#board");

const winningMessage = document.querySelector("#winning-message");
const winningMessageText = document.querySelector("[data-winning-message-text]");

const restartButton = document.querySelector("#restart");

restartButton.addEventListener("click", init);

let isCircleTurn;

function init() {
    isCircleTurn = false;

    cells.forEach(cell => {
        cell.classList.remove(X_CLASS);
        cell.classList.remove(CIRCLE_CLASS);

        cell.removeEventListener("click", onClick);

        cell.addEventListener("click", onClick, { once: true });
    });

    handleSetBoardHoverClass();

    winningMessage.classList.remove("show");
}

init();

function onClick(event) {
    const cell = event.target;

    const currentClass = isCircleTurn ? CIRCLE_CLASS : X_CLASS;

    handlePlaceMark({ cell, currentClass });

    if (didUserWin(currentClass)) {
        handleEndGame(false);
    }

    else if (isADraw()) {
        handleEndGame(true);
    }

    else {
        handleSwapTurns();
        handleSetBoardHoverClass();
    }
}

function isADraw() {
    return [...cells].every(cell => {
        return cell.classList.contains(X_CLASS) || cell.classList.contains(CIRCLE_CLASS);
    });
}

function didUserWin(currentClass) {
    return WINNING_COMBINATIONS.some(combination => {
        return combination.every(index => {
          return cells[index].classList.contains(currentClass)
        })
    });
}

function handleEndGame(isDraw) {
    if (isDraw) {
        winningMessageText.textContent = "Deu empate!";
    }

    else {
        winningMessageText.textContent = `${isCircleTurn ? "O's" : "X's"} venceu!`; 
    }

    winningMessage.classList.add("show");
}
 
function handlePlaceMark({ cell, currentClass }) {
    cell.classList.add(currentClass);
}

function handleSwapTurns() {
    isCircleTurn = !isCircleTurn;
}

function handleSetBoardHoverClass() {
    board.classList.remove(X_CLASS);
    board.classList.remove(CIRCLE_CLASS);

    if (isCircleTurn) {
        board.classList.add(CIRCLE_CLASS);
    }

    else {
        board.classList.add(X_CLASS);
    }
}