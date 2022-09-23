# TP

## Goals

- Get familiar with JavaScript
- Make API requests using JavaScript frontend
- Get familiar with CSS styling

## Before starting

1. Run `docker-compose up -d --build`
2. Run `docker-compose exec front bash` to remote exec into the front container
3. Run `npm install` to install required packages
4. Run `npm run dev` to start the development server
5. Open `localhost:3000` in your browser

The file to edit is `tp_front/front/src/routes/+page.svelte`.

For more information about how the frontend environment is set up: [Frontend setup](#frontend-setup)

## Make API requests


1. Send a GET request to https://jsonplaceholder.typicode.com/todos/1 and print result in terminal using:
    - fetch [docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
2. Display result in page using:
    - variable declaration: [const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) and [let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    - [async/await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises#async_and_await) to write an asynchronous function
    - [svelte if statement](https://svelte.dev/tutorial/if-blocks) and [if-else](https://svelte.dev/tutorial/else-if-blocks) statements to display variable only if it is not null
    - note: response data is an [object](https://dmitripavlutin.com/access-object-properties-javascript/), which is like a Python [dictionary](https://www.w3schools.com/python/python_dictionaries.asp)
3. Display result when clicking on button using:
    - [svelte event modifier](https://svelte.dev/tutorial/event-modifiers) to call function when clicking button. Copy this svelte button element
    ```
    <button
		class="m-3 p-3 text-white bg-green-400"
		on:click={null}
	>
		button
	</button>
    ```
4. Send a GET request to https://jsonplaceholder.typicode.com/todos and display list of results in page using:
    - [svelte each statement](https://svelte.dev/tutorial/each-blocks) to loop through array of results
5. Send a GET request to the API container:
    - instead of using the service name, the URL should be `http://localhost:port`. It is because the API is called from the client browser, therefore it is reached with `localhost` instead of its service name (when from inside the docker compose network).
    - note: the API requires [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) to be enabled because it is by default not permitted for an API to be requested using localhost.
6. Send a POST request to the API container:
    - route `/job` with parameters `title`, `company`, `salary` (see `tp_front/api/app.py`)

## Style page

Play around with:
- [text color](https://tailwindcss.com/docs/text-color)
- [font size](https://tailwindcss.com/docs/font-size)
- [font weight](https://tailwindcss.com/docs/font-weight)
- button [background color](https://tailwindcss.com/docs/background-color)
- button [border radius](https://tailwindcss.com/docs/border-radius)

## Frontend setup

Steps used for setting up the frontend container.

See [Svelte docs](https://kit.svelte.dev/), [TailwindCSS docs](https://github.com/svelte-add/tailwindcss).

### Install Svelte Kit

- `npm create svelte@latest front`. Selected features
    - Project: Skeleton project
    - TypeScript: no
    - ESLint linting: yes
    - Prettier formatting: yes
    - Playright testing: no
- `cd front`
- `npm install`

### Install TailwindCSS

- `npx svelte-add@latest tailwindcss`