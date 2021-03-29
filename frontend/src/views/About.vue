<template>
  <div class="about">
    <h1>Hello 2</h1>
    <p>{{ content }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import api from '../api/api'

export default {
  name: 'About',
  data() {
    return {
      content: '',
    }
  },

  methods: {
    fetchContent() {
      axios.get(api.URL + api.ROUTES.hello2)
        .then(res => this.content = res.data.content)
        .catch(err => console.error(err))
    },
  },

  mounted() {
    this.fetchContent()
  },
}
</script>

