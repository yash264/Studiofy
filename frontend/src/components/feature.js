import { useState } from "react";

function Section() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [resultImage, setResultImage] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleImageChange = (e) => {
        const selectedFile = e.target.files[0];
        if (!selectedFile) return;

        setFile(selectedFile);
        setPreview(URL.createObjectURL(selectedFile));
        setResultImage(null);
        setError(null);
    };

    const handleEnhance = async () => {
        if (!file) {
            setError("Please select an image first");
            return;
        }

        setLoading(true);
        setError(null);
        setResultImage(null);

        const formData = new FormData();
        formData.append("image", file);

        try {
            const response = await fetch("http://127.0.0.1:5000/enhance", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("Enhancement failed");
            }

            const blob = await response.blob();
            const imageURL = URL.createObjectURL(blob);
            setResultImage(imageURL);
        } 
        catch(err){
            console.error(err);
            setError("Server not reachable");
        } 
        finally{
            setLoading(false);
        }
    };

    return (
        <>
            <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 gap-6 md:grid-cols-2 md:items-center">

                    {/* LEFT SIDE */}
                    <div className="p-4">
                        <label className="inline-block cursor-pointer rounded bg-rose-500 px-4 py-2 text-white font-bold hover:bg-rose-600">
                            Select Image
                            <input
                                type="file"
                                accept="image/*"
                                onChange={handleImageChange}
                                className="hidden"
                            />
                        </label>

                        {preview && (
                            <div className="mt-6 space-y-4">
                                <img
                                    src={preview}
                                    alt="Original Preview"
                                    className="max-w-full rounded-lg shadow-lg"
                                />

                                <button
                                    onClick={handleEnhance}
                                    disabled={loading}
                                    className={`rounded px-4 py-2 text-white font-bold ${loading
                                        ? "bg-gray-400"
                                        : "bg-green-500 hover:bg-green-600"
                                        }`}
                                >
                                    {loading ? "Processing..." : "Enhance Portrait"}
                                </button>

                                {error && <p className="text-red-500">{error}</p>}
                            </div>
                        )}
                    </div>

                    {/* RIGHT SIDE */}
                    <div className="space-y-6">
                        {resultImage ? (
                            <div>
                                <h2 className="mb-2 text-xl font-bold text-gray-800">
                                    Enhanced Result
                                </h2>
                                <img
                                    src={resultImage}
                                    alt="Enhanced Output"
                                    className="w-full rounded-lg shadow-lg border border-gray-200"
                                />
                            </div>
                        ) : (
                            <div className="flex flex-col items-center justify-center h-full">
                                <img
                                    src="https://media.istockphoto.com/id/1324356458/vector/picture-icon-photo-frame-symbol-landscape-sign-photograph-gallery-logo-web-interface-and.jpg?s=612x612&w=0&k=20&c=ZmXO4mSgNDPzDRX-F8OKCfmMqqHpqMV6jiNi00Ye7rE="
                                    alt="Placeholder"
                                    className="w-64 rounded-lg shadow-lg opacity-50"
                                />
                                <p className="mt-4 text-gray-500">
                                    {preview
                                        ? "Click enhance to generate studio-quality image"
                                        : "Upload a portrait to begin"}
                                </p>
                            </div>
                        )}
                    </div>

                </div>
            </div>
        </>
    );
}

export default Section;
