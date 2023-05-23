<template>
  <div>

  </div>
</template>

<script>
export default {
    name:'WaitIng',
    data(){
        return{
            movie_id : null,
        }
    },
    created(){
        this.$router.go(this.$router.currentRoute)
        console.log('hi')
    }
}
</script>

<style>

</style>