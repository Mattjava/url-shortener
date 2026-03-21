const restext = document.getElementById('result-text');
const textin = document.getElementById('url-box');
const submit_button = document.getElementById('submit_button');


submit_button.addEventListener('click', function() {
    console.log(restext.textContent);
    console.log(textin.value);
    restext.textContent = textin.value;
})