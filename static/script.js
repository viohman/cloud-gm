document.addEventListener('DOMContentLoaded', function() {
    const rollD100Button = document.getElementById('roll_d100_button');
    const diceResultDiv = document.getElementById('dice_result');

    if (rollD100Button) {
        rollD100Button.addEventListener('click', function() {
            diceResultDiv.textContent = 'Rolling...';
            fetch('/roll_dice/d100')
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        diceResultDiv.textContent = `Error: ${data.error}`;
                    } else {
                        diceResultDiv.textContent = `Rolled ${data.dice_type}: ${data.result}`;
                        // Optionally, you could also update a more general game log on the page
                        // if you had one, using data.log_message
                        console.log(data.log_message); // Log to browser console for now
                    }
                })
                .catch(error => {
                    console.error('Error rolling dice:', error);
                    diceResultDiv.textContent = 'Error rolling dice. Check console.';
                });
        });
    }
});
