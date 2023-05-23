<template>
  <div>
    <p>{{ $route.params.user_id }}</p>
    <p>{{ $route.params.username }}</p>
  </div>
</template>

<script>

export default {
    name: 'OtherUserProfile',
    data() {
        return{
            
        }
    }
}
</script>

<style>

</style>