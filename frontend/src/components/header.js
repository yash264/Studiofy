import { Design } from "../assets/design";

function Banner() {
    return (
        <>
            <section className="bg-white lg:grid lg:h-screen lg:place-content-center">

                <div className="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8 lg:py-32">

                    <div className="grid gap-12 lg:grid-cols-2 items-center">
                        {/* Image - LEFT */}
                        <div className="flex justify-center lg:justify-start">
                            <Design />
                        </div>

                        {/* Text - RIGHT */}
                        <div className="mx-auto max-w-prose align-center lg:text-left">
                            <h1 className="text-4xl font-bold text-gray-900 sm:text-5xl">
                                <strong className="text-indigo-600"> StudioFy </strong>
                                a Portrait Enhancer
                            </h1>

                            <p className="mt-4 text-base text-pretty text-gray-700 sm:text-lg/relaxed">
                                Studiofy is a lightweight computer vision–based system that transforms raw, everyday photos into studio-style portraits.
                            </p>

                            <p className="mt-4 text-base text-pretty text-gray-700 sm:text-lg/relaxed">
                                It enhances facial clarity, improves color and contrast, and applies realistic background blur while preserving natural skin texture and original identity.
                            </p>

                            <div className="mt-6 flex align-center gap-4 lg:justify-start">
                                <a
                                    className="inline-block rounded border border-green-600 bg-green-600 px-5 py-3 font-medium text-white shadow-sm transition-colors hover:bg-rose-600"
                                    href="#feature"
                                >
                                    Get Started
                                </a>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        </>
    )
}

export default Banner;