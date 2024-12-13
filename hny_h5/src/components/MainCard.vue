<template>
    <div ref="card_con" class="relative left-0 top-0 transition-all duration-[1500ms] ease">
        <div ref="card_main" class="w-20 h-20    
            relative transform-3d
            transition-all ease-in-out duration-[1500ms]"
            @click.stop="switch_flip">
            <div class="w-full h-full top-1/2 left-1/2 absolute
                -translate-x-1/2 -translate-y-1/2 transition-all ease-in-out duration-1000
                backface-hidden bg-center bg-no-repeat text-white bg-blue-500"
                :class="{'z-20': !flip_state, '-z-20': flip_state}">1</div>
            <div class="w-full h-full top-1/2 left-1/2 absolute
                -translate-x-1/2 -translate-y-1/2 transition-all ease-in-out duration-1000
                backface-hidden bg-center bg-no-repeat text-white bg-red-500 rotate-y-180"
                :class="{'z-20': flip_state, '-z-20': !flip_state}">2</div>
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, nextTick } from 'vue';

export default defineComponent({
    name: 'MainCard',
    setup() {
        const flip_state = ref(false);
        const center_state = ref(false);
        const card_con = ref(null);
        const card_main = ref(null);

        const moveToCenter = (el,mode) => {
            if (!el) return;

            if (!mode) {
                const rect = el.getBoundingClientRect();
                const parent_rect = el.parentNode.getBoundingClientRect();
                // console.log('son', rect)
                // console.log('parent', parent_rect)
                const newX = (parent_rect.width - rect.width)/2 + (parent_rect.left - rect.left)
                const newY = (parent_rect.height - rect.height)/2 + (parent_rect.top - rect.top)

                el.style.left = `${newX}px`;
                el.style.top = `${newY}px`;
            } else {
                el.style.left = 0;
                el.style.top = 0;
            }
        };

        const switch_flip = () => {
            const container = card_main.value;
            container.style.transform = flip_state.value ? 'scale(1)' : 'rotateY(180deg) scale(2)';
            const con_big = card_con.value;
            moveToCenter(con_big, flip_state.value)
            nextTick().then(()=>{
                flip_state.value = !flip_state.value
            })
        };

        return { flip_state, center_state, card_main, card_con, 
            switch_flip, moveToCenter };
    }
    
})
</script>