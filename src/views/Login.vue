<template>
  <div class="container">
    <form action="#" v-on:submit="submitLogin">
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" type="email" ref="email" />
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" type="password" ref="password" />
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button" v-on:click="submitLogin">Login</button>
        </div>
      </div>

    </form>
  </div>
</template>

<script>
import backendUrl from '@/settings.js'
import axios from 'axios'

axios.defaults.withCredentials = true

export default {
  name: 'login',
  methods: {
    submitLogin: function () {
      const comp = this
      const email = this.$refs.email.value
      const pw = this.$refs.password.value
      axios.post(backendUrl + '/login', { email: email, pw: pw })
        .then((res) => {
          comp.$router.push('/')
          return false
        })
        .catch(() => {
          return false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
form {
  margin: 0 auto;
}
</style>
