<template>
  <div class="content">
    <form class="box">
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" type="email" />
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" type="password" />
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button">Login</button>
        </div>
      </div>

    </form>
  </div>
</template>

<script>
export default {
  name: 'login'
}
</script>

<style lang="scss">
form {
  margin: 0 auto;
  max-width: 800px;
}
</style>
