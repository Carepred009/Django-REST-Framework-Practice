<template>
  <div>
    <updateData_FK :productId="productId" />
  </div>
</template>

<script>
import updateData_FK from "../components/updateData_FK.vue";

export default {
  props: ['productId'],   // receives from router
  components: {
    updateData_FK
  }
}
</script>
