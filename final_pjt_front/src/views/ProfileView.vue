<template>
  <div>
    <p>{{ user_data.pk }}</p>
    <p>{{ user_data.username }}</p>
  </div>
</template>

<script>
export default {
    name: 'ProfileView',
    data() {
        return{
            user_data : this.$store.state.user_data
        }
    }
}
</script>

<style>

</style>