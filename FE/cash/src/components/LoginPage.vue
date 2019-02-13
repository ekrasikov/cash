<template>
  <div>
    <h1>Hey</h1>
    <div v-if="!isLoggedIn()">
      <h2>Login:</h2>
      <button class="button is-primary is-large is-fullwidth" @click="login()">Login</button>
    </div>
    <div v-if="isLoggedIn()">
      <h2>Logout:</h2>
      <button class="button is-danger is-large is-fullwidth" @click="logout()">Logout</button>
    </div>
  </div>
</template>

<script>
import auth from '../utils/auth'

export default {
  name: 'LoginPage',
  methods: {
    login () {
      auth.login()
    },
    logout () {
      auth.logout()
    },
    isLoggedIn () {
      return auth.isAuthenticated()
    }
  }
}
</script>
