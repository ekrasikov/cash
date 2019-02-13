<template>
  <div>
    Logged in
  </div>
</template>

<script>

export default {
  name: 'Callback',
  props: ['auth'],
  created () {
    this.auth.handleAuthentication()
  }
}
</script>
