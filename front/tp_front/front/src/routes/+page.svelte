<script>
    console.log("hello from terminal");
    let todo;
    async function getTodo() {
        fetch("https://jsonplaceholder.typicode.com/todos/1")
        // fetch("http://localhost:5000/")
            .then((response) => response.json())
            .then((data) => {
                console.log("prout");
                console.log(data);
                todo = data;
            })
            .catch((error) => console.log(error)
        );
    }
    // getTodo();
</script>

<div class="flex justify-center justify-items-center grid grid-flow-row auto-rows-max p-10">
    <p>Hello there</p>
    <a class="underline" href="https://svelte.dev/tutorial/basics">Link to Svelte tutorial</a>
    <a class="underline" href="https://tailwindcss.com/docs/text-color">Link to Tailwind CSS docs</a>
    <button
    class="m-3 p-3 text-white bg-green-400"
    on:click={getTodo}
	>
    button
</button>
    {#if todo}
        <p>{todo["title"]}</p>
    {/if}
</div>