type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    events: Map<string, Callback[]>

    constructor() {
        this.events = new Map()
    }

    subscribe(eventName: string, callback: Callback): Subscription {
        this.events.set(eventName, [...(this.events.get(eventName) || []), callback])
        return {
            unsubscribe: () => {
                const callbacks = this.events.get(eventName)

                if (callbacks) {
                    this.events.set(eventName, callbacks.filter((cb) => cb !== callback))
                }
            }
        };
    }

    emit(eventName: string, args: any[] = []): any[] {
        const callbacks = this.events.get(eventName)
        if (!callbacks) {
            return []
        }
        return callbacks.map((callback) => callback(...args))
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */