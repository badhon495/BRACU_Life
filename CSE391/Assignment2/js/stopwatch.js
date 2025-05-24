let timer;
let time = 0;

document.getElementById('start').addEventListener('click', () => {
    if (!timer) {
        timer = setInterval(() => {
            time += 3;
            if (time > 30) {
                clearInterval(timer);
                timer = null;
                time = 0;
                
            }
            document.getElementById('display').innerText = time;
        }, 1000);
    }
});

document.getElementById('stop').addEventListener('click', () => {
    clearInterval(timer);
    timer = null;
    time=0;
});

document.getElementById('reset').addEventListener('click', () => {
    clearInterval(timer);
    timer = null;
    time = 0;
    document.getElementById('display').innerText = time;
});
