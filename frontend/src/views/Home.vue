<template>
  <div class="home">
    <h1>Hello</h1>
    <p>{{ content }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import api from '../api/api'

export default {
  name: 'Home',
  data() {
    return {
      content: '',
    }
  },

  methods: {
    fetchMessage() {
      axios.get(api.URL + api.ROUTES.hello)
        .then(res => this.content = res.data.content)
        .catch(err => console.error(err))
    },
  },

  mounted() {
    this.fetchMessage()
  },
}
</script>
