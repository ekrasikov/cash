<template>
  <div class="callback">
    Logging in...
  </div>
</template>

<script>
import auth from '../utils/auth.js'

export default {
  name: 'Callback',
  created () {
    auth.handleAuthentication()
  }
}
</script>
