let userScore = 0;
let computerScore = 0;

function getComputerChoice() {
  const choices = ["snake", "water", "gun"];
  return choices[Math.floor(Math.random() * choices.length)];
}

function determineWinner(userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return "It's a Tie!";
  } else if (
    (userChoice === "gun" && computerChoice === "snake") ||
    (userChoice === "snake" && computerChoice === "water") ||
    (userChoice === "water" && computerChoice === "gun")
  ) {
    userScore++;
    return "You Win!";
  } else {
    computerScore++;
    return "Computer Wins!";
  }
}

function playGame(userChoice) {
  const computerChoice = getComputerChoice();
  const result = determineWinner(userChoice, computerChoice);

  document.getElementById("result").innerHTML =
    `You chose <b>${userChoice}</b> | Computer chose <b>${computerChoice}</b><br>${result}`;

  document.getElementById("score").innerHTML =
    `Score → You: ${userScore} | Computer: ${computerScore}`;
}
