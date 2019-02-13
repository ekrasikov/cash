<template>
  <div>
    <div v-if="!authenticated">
      <button class="button is-primary is-large is-fullwidth" @click="auth.login()">Login</button>
    </div>
    <div v-if="authenticated">
      <button class="button is-danger is-large is-fullwidth" @click="auth.logout()">Logout</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LoginPage',
  props: ['auth', 'authenticated']
}
</script>
