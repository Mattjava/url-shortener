import { useState } from 'react';

function MainContainer() {
    const [url, setUrl] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [shortenedUrl, setShortenedUrl] = useState('');

    function handleSubmit() {
        if (url == '') {
            console.log("Empty");
            return;
        }
        setSubmitted(true);
        setShortenedUrl(url);

    }

    return (
        <div className="min-h-screen bg-blue-100 flex items-center justify-center">
            <div className="bg-white rounded-2xl shadow-lg p-8 w-80">
                <h1 className="font-bold text-center text-2xl mb-10">Shortify</h1>
                <input
                    value={url}
                    onChange = {(e) => setUrl(e.target.value)}
                    placeholder = "Enter a URL."
                    className="w-full border border-gray-800 rounded-lg px-4 py-2"
                ></input>
                <button onClick={handleSubmit}
                    className="w-full bg-gray-100 rounded-2xl mt-6 py-2 font-semibold text-black transition hover:bg-blue-500">
                    Submit</button>
                {submitted && 
                    <text className="font-bold to-blue-200 flex items-center justify-center my-3">Result: {shortenedUrl}</text>
                }
            </div>
        </div>
    );
};

export default MainContainer;