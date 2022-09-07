<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button v-on:click="getApiResponse()">Make API request</button>
    <p>{{ apiResponse }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data: () => ({
    apiResponse: "Request me!",
  }),
  methods: {
    getApiResponse() {
      const axios = require('axios');
      axios.get('http://localhost:5000/')
      // axios.get('https://jsonplaceholder.typicode.com/posts/1')
        .then(response => response.data)
        .then(data => { 
          console.log(data);
          this.apiResponse = data;
        });
        // .catch(err => console.log(err));
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
