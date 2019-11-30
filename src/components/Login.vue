<template>
  <div class="modal" ref="main" :class="{ 'is-active': isActive }">
    <div class="modal-background"></div>
    <div class="modal-content">
      <form class="box" action="#" v-on:submit="submitLogin">
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
  </div>
</template>

<script>
import backendUrl from '@/../settings.js'
import axios from 'axios'

axios.defaults.withCredentials = true

export default {
  name: 'login',
  methods: {
    submitLogin: function () {
      const email = this.$refs.email.value
      const pw = this.$refs.password.value
      axios.post(backendUrl + '/login', { email: email, pw: pw })
        .then((res) => {
          this.$emit('login', true)
          return false
        })
        .catch(() => {
          this.$emit('login', false)
          return false
        })
    }
  },
  props: {
    isActive: Boolean
  }
}
</script>

<style lang="scss" scoped>
form {
  margin: 0 auto;
}
</style>
