<template>
    <div ref="card_con" class="relative transition-all left-0 top-0 duration-[2000ms] ease">
        <div ref="card_element" class="w-20 h-20    
            relative transform-3d
            transition-all ease-in-out duration-[1500ms]"
            @click.stop="switch_flip">
            <div class="w-full h-full top-1/2 left-1/2 absolute
                -translate-x-1/2 -translate-y-1/2 transition-all ease-in-out duration-1000
                backface-hidden bg-center bg-no-repeat text-white bg-blue-500"
                :class="{'z-20': !flipState, '-z-20': flipState}">1</div>
            <div class="w-full h-full top-1/2 left-1/2 absolute
                -translate-x-1/2 -translate-y-1/2 transition-all ease-in-out duration-1000
                backface-hidden bg-center bg-no-repeat text-white bg-red-500 rotate-y-180"
                :class="{'z-20': flipState, '-z-20': !flipState}">2</div>
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, nextTick } from 'vue';

export default defineComponent({
    name: 'MainCard',
    setup() {
        const flipState = ref(false);
        const centerState = ref(false);
        const card_element = ref(null);
        const card_con = ref(null);

        const moveToCenter = (el) => {
            if (!el) return;
            const vp_width = window.innerWidth || document.documentElement.clientWidth;
            const vp_height = window.innerHeight || document.documentElement.clientHeight;

            console.log(vp_width, vp_height)
            console.log(window.innerWidth)

            const rect = el.getBoundingClientRect();
            // el.style.top = rect.top
            el.style.left = rect.left
            const newX = (vp_width + rect.width) / 2;
            // const newY = (vp_height + rect.height) / 2;
            // el.style.position = 'fixed';
            // el.style.transition = 'top 1.5s, left 1.5s'
            // el.style.top = `${newY}px`;
            el.style.left = `${newX}px`;
        };

        const switch_flip = () => {
            const container = card_element.value;
            container.style.transform = flipState.value ? 'scale(1)' : 'rotateY(180deg) scale(2)';
            const con_big = card_con.value;
            moveToCenter(con_big)
            nextTick().then(()=>{
                flipState.value = !flipState.value
            })
        };
        return { card_element, card_con, switch_flip, flipState, centerState, moveToCenter };
    }
    
})
</script>