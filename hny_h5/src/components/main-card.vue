<template>
    <div class="container" id="container" @click="switch_flip">
        <div class="rp front" ></div>
        <div class="rp back" ></div>
    </div>
</template>

<style>
.container {
    width: 200px;
    height: 400px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 1.5s ease-in-out;
}
.rp {
    left: 0;
    top: 0;
    position: absolute;
    backface-visibility: hidden;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    width: 100%;
    height: 100%;
}
.front {
    background-color: red;
}
.back {
    background-color: blue;
    transform: rotateY(-180deg);
}

</style>

<script>
import { defineComponent, ref } from 'vue';


export default defineComponent({
    name: 'MainCard',
    setup() {
        const flipState = ref(false);

        const switch_flip = () => {
            const container = document.getElementById('container');
            container.style.transform = flipState.value ? 'rotateY(0deg) scale(1)' : 'rotateY(180deg) scale(2)';
            flipState.value = !flipState.value
        };
        return { switch_flip, flipState };
    }
    
})

</script>